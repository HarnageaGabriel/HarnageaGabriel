#!/usr/bin/env python3
"""Render README.md (English) and README.it.md (Italian) from one source.

The contribution tables come from the GitHub search API through `gh`, so the
counts and the pull request list never have to be updated by hand.

    python scripts/render_readme.py

Requires `gh` on PATH and authenticated, or GH_TOKEN in the environment.
"""

import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import badges

USER = "HarnageaGabriel"
PLUGIN_VERSION = "v0.3.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = "https://raw.githubusercontent.com/%s/%s/main" % (USER, USER)

# Rows without an entry render with an empty icon cell. Simple Icons dropped
# the Microsoft marks, so Azure repositories have no icon on purpose.
ICONS = {
    "kubernetes": "kubernetes/326CE5", "kubernetes-sigs": "kubernetes/326CE5",
    "moby": "docker/2496ED", "docker": "docker/2496ED",
    "argoproj": "argo/EF7B4D", "containerd": "containerd/575757",
    "dotnet": "dotnet/512BD4", "nunit": "dotnet/512BD4", "NLog": "dotnet/512BD4",
    "quartznet": "dotnet/512BD4", "nsubstitute": "dotnet/512BD4",
    "DapperLib": "dotnet/512BD4", "StackExchange": "redis/FF4438",
    "BurntSushi": "rust/DEA584", "tokio-rs": "rust/DEA584",
    "rust-embedded": "rust/DEA584", "dtolnay": "rust/DEA584",
    "ansible": "ansible/EE0000", "traefik": "traefikproxy/24A1C1",
    "dotnet-outdated": "nuget/004880", "saltstack": "saltproject/57BCAD",
    "thanos-io": "thanos/6D49FF", "spiffe": "cncf/231F20",
    "open-policy-agent": "cncf/231F20",
}

# Repositories are listed in this order; anything unlisted goes last.
MERGED_ORDER = [
    "dotnet/runtime", "kubernetes-sigs/apiserver-network-proxy",
    "StackExchange/StackExchange.Redis", "DapperLib/DapperAOT", "nunit/nunit-console",
]
OPEN_ORDER = [
    "moby/moby", "kubernetes/kube-openapi", "kubernetes-sigs/krew-index",
    "kubernetes/perf-tests", "docker/cli", "containerd/runwasi", "argoproj/argo-cd",
    "argoproj/argo-rollouts", "argoproj/argo-workflows", "open-policy-agent/opa",
    "spiffe/spire", "thanos-io/objstore", "saltstack/salt", "BurntSushi/ripgrep",
    "tokio-rs/tracing", "dtolnay/cxx", "rust-embedded/heapless", "dotnet/runtime",
    "dotnet/msbuild", "StackExchange/StackExchange.Redis", "quartznet/quartznet",
    "NLog/NLog", "nsubstitute/NSubstitute", "dotnet-outdated/dotnet-outdated",
    "ansible/terraform-provider-aap", "traefik/traefik-helm-chart",
    "Azure/azure-powershell",
]

# Titles carry conventional-commit prefixes and shorthand. Spell them out.
REWRITES = {
    "c8d/resolver: reuse per-host authorizers across a pull":
        "Reuse per-host authorizers across a pull in the c8d resolver",
    "registry: normalize server address to lowercase for credential lookup":
        "Normalize the registry server address to lowercase for credential lookup",
    "gcs: support custom GCS API endpoint via endpoint config option":
        "Support a custom GCS API endpoint through the endpoint config option",
    "search-zip: detect compressed files by magic number, not just extension":
        "Detect compressed files by magic number in search-zip, not just by extension",
    "ignore: fix dangling backslash error for escaped trailing space with extra spaces":
        "Fix the dangling backslash error for an escaped trailing space",
    "subscriber: add opt-in field value truncation wrapper":
        "Add an opt-in field value truncation wrapper to the subscriber",
    "DateLayoutRenderer - Changed default Format to yyyy-MM-dd HH:mm:ss.ffff":
        "Change the DateLayoutRenderer default format to yyyy-MM-dd HH:mm:ss.ffff",
    "test(clusterloader2): add unit tests for pkg/errors":
        "Add unit tests for clusterloader2/pkg/errors",
    "Report packages whose source repo is archived or deleted (GitHub only)":
        "Report packages whose source repository is archived or deleted",
}


def fetch_pull_requests():
    out = subprocess.check_output([
        "gh", "api", "-X", "GET", "search/issues",
        "-f", "q=author:%s type:pr" % USER, "-f", "per_page=100",
        "--jq", '[.items[] | {repo:(.repository_url|split("/")|.[-2:]|join("/")), '
                'number, state, merged:(.pull_request.merged_at!=null), title, url:.html_url}]',
    ], shell=(os.name == "nt"))
    prs = json.loads(out.decode("utf-8"))
    return [p for p in prs if not p["repo"].startswith(USER + "/")]


def describe(title):
    if title in REWRITES:
        return REWRITES[title]
    text = re.sub(r"^\s*(fix|feat|test|chore|docs|security|refactor)(\([^)]*\))?:\s*", "", title)
    text = re.sub(r"\s*\(#\d+\)\s*$", "", text)
    return text[0].upper() + text[1:]


def icon_cell(repo):
    slug = ICONS.get(repo.split("/")[0])
    if not slug:
        return ""
    return '<img src="https://cdn.simpleicons.org/%s" width="18"/>' % slug


def table(rows, headers):
    lines = ["| | %s | %s | %s |" % headers, "|:-:|---|---|:-:|"]
    for p in rows:
        lines.append("| %s | **%s** | %s | [`#%d`](%s) |" % (
            icon_cell(p["repo"]), p["repo"], describe(p["title"]), p["number"], p["url"]))
    return "\n".join(lines)


def ordered(rows, preferred):
    return sorted(rows, key=lambda p: (
        preferred.index(p["repo"]) if p["repo"] in preferred else 99, p["repo"], -p["number"]))


EN = {
    "lang": "en",
    "location": "TURIN, ITALY",
    "lang_note": ('<img src="%s/assets/lang-en-on.svg?v=3" alt="English" />'
                  '&nbsp;<a href="README.it.md"><img src="%s/assets/lang-it-off.svg?v=3" alt="Italiano" /></a>') % (RAW, RAW),
    "about": "About",
    "about_body": """I'm a DevOps & Platform Engineer on enterprise projects: CI/CD, Kubernetes, Terraform, cloud cost.

I wrote application code before I ran the infrastructure that hosts it, which pays off mostly when a build breaks and someone has to know where to look.

The open-source work here comes from the same place. Something misbehaves in a real deployment, I go read the source, and the fix goes upstream rather than into a patch I keep to myself.""",
    "yaml": """role:      DevOps & Platform Engineer
platform:  [Azure, Kubernetes, GitOps, Terraform, Azure DevOps, GitHub Actions]
also:      [FinOps, Agentic DevOps, .NET backend]
languages: [C#, TypeScript, Go, Rust, Python, Bash, PowerShell]
into:      [correctness bugs, observability gaps, release plumbing, cloud cost]
based_in:  Turin, Italy""",
    "what": "What I do",
    "cells": [
        ("githubactions", "Pipelines", "Azure DevOps · GitHub Actions · templates"),
        ("kubernetes", "Kubernetes", "AKS · k3d · Helm · Helmfile"),
        ("terraform", "Infrastructure", "Terraform · scale sets · golden images"),
        ("docker", "Containers", "Docker · Helm charts · OCI on ACR/GHCR"),
        ("azure", "Cloud &amp; cost", "Azure · reservations · FinOps"),
        ("dotnet", "Backend", ".NET 8/9 · CQRS · DDD"),
    ],
    "stack": "Stack",
    "stack_blocks": [
        ("Platform &amp; CI/CD", "Azure DevOps YAML pipelines and reusable templates · GitHub Actions · Helm charts and Helmfile releases · OCI push to ACR/GHCR · ApiOps policy automation on Azure API Management · Jinja2 templating · branch policies, PR review, code review as a gate"),
        ("Cloud &amp; infrastructure", "Kubernetes on AKS and k3d on-prem · NGINX Ingress Controller · Terraform (azurerm, azuredevops) · VM Scale Sets as self-hosted agent pools · golden images for faster scale-out · Container Registry, Storage Accounts, Functions, Entra · reservation and cost governance"),
        ("Backend &amp; architecture", "REST/HTTP APIs in .NET 8/9 · Worker Services · CQRS with MediatR · Domain-Driven Design · hexagonal and N-tier architectures · API gateway with Ocelot · EF Core and Dapper · PostgreSQL, MongoDB · NUnit + Moq, self-hosted integration tests"),
        ("Identity, storage &amp; AI", "Keycloak with OAuth 2.0 · JWT bearer flows · SeaweedFS through the S3-compatible client · self-hosted LLM inference with Ollama · RAG pipelines with ChromaDB and embedding models · Copilot governance and AI spend controls"),
    ],
    "upstream": "Upstream contributions",
    "upstream_lead": "%d pull requests across %d projects I run or depend on. %d merged so far, %d still in review.",
    "merged": "Merged",
    "in_review": "In review",
    "in_review_count": "(%d open pull requests)",
    "headers": ("Project", "Change", "PR"),
    "all_prs": "See all pull requests",
    "projects": "Projects",
    "projects_headers": "| | Project | What it is | Stack | |\n|:-:|---|---|---|:-:|",
    "projects_rows": [
        ("kubectl-safe-rollout", "A kubectl plugin that tells you why a rollout failed or stalled. Deterministic classification, no LLM, and it never writes to the cluster", "`Go` `client-go`", "`v0.3.0`"),
        ("github-actions-recipes", "The workflows behind my CI/CD and FinOps posts, one variable isolated per recipe", "`GitHub Actions`", "`live`"),
        ("token-optimization", "Cuts token usage when working with LLM coding agents. Re-running the setup is a no-op", "`PowerShell`", "`live`"),
    ],
    "krew_note": "`kubectl-safe-rollout` is [submitted to krew-index](https://github.com/kubernetes-sigs/krew-index/pull/6213), so it will be installable with `kubectl krew install safe-rollout`.",
    "writing": "Writing",
    "writing_body": "I write on LinkedIn about platform details that usually pass unchecked: how Azure DevOps resolves its three expression syntaxes, the compliance rules for self-hosted runners, what Copilot code review does and does not decide, and whether an Azure reservation discount is still applying to anything.",
    "read_linkedin": "Read on LinkedIn",
    "footer_cta": "Get in touch",
    "badge_merged": "MERGED UPSTREAM",
    "badge_projects": "PROJECTS TOUCHED",
    "badge_plugin": "KUBECTL PLUGIN",
    "views": "PROFILE VIEWS",
}

IT = {
    "lang": "it",
    "location": "TORINO, ITALIA",
    "lang_note": ('<a href="README.md"><img src="%s/assets/lang-en-off.svg?v=3" alt="English" /></a>'
                  '&nbsp;<img src="%s/assets/lang-it-on.svg?v=3" alt="Italiano" />') % (RAW, RAW),
    "about": "Chi sono",
    "about_body": """Sono un DevOps & Platform Engineer su progetti enterprise: CI/CD, Kubernetes, Terraform, costi cloud.

Ho scritto codice applicativo prima di gestire l'infrastruttura che lo ospita, e questo serve soprattutto quando una build si rompe e qualcuno deve sapere dove guardare.

Il lavoro open source qui sopra nasce allo stesso modo. Qualcosa si comporta male in un deployment reale, vado a leggere il sorgente, e la correzione finisce upstream invece che in una patch che tengo per me.""",
    "yaml": """ruolo:     DevOps & Platform Engineer
platform:  [Azure, Kubernetes, GitOps, Terraform, Azure DevOps, GitHub Actions]
anche:     [FinOps, Agentic DevOps, backend .NET]
linguaggi: [C#, TypeScript, Go, Rust, Python, Bash, PowerShell]
mi_occupo: [bug di correttezza, buchi di osservabilità, release plumbing, costi cloud]
dove:      Torino, Italia""",
    "what": "Di cosa mi occupo",
    "cells": [
        ("githubactions", "Pipeline", "Azure DevOps · GitHub Actions · template"),
        ("kubernetes", "Kubernetes", "AKS · k3d · Helm · Helmfile"),
        ("terraform", "Infrastruttura", "Terraform · scale set · golden image"),
        ("docker", "Container", "Docker · Helm chart · OCI su ACR/GHCR"),
        ("azure", "Cloud e costi", "Azure · reservation · FinOps"),
        ("dotnet", "Backend", ".NET 8/9 · CQRS · DDD"),
    ],
    "stack": "Stack",
    "stack_blocks": [
        ("Platform e CI/CD", "Pipeline YAML e template riusabili su Azure DevOps · GitHub Actions · Helm chart e rilasci con Helmfile · push OCI su ACR/GHCR · automazione delle policy con ApiOps su Azure API Management · templating Jinja2 · branch policy, pull request e code review come gate"),
        ("Cloud e infrastruttura", "Kubernetes su AKS e k3d on-prem · NGINX Ingress Controller · Terraform (azurerm, azuredevops) · VM Scale Set come agent pool self-hosted · golden image per scalare più in fretta · Container Registry, Storage Account, Functions, Entra · governo di reservation e costi"),
        ("Backend e architettura", "API REST/HTTP in .NET 8/9 · Worker Service · CQRS con MediatR · Domain-Driven Design · architetture esagonali e N-tier · API gateway con Ocelot · EF Core e Dapper · PostgreSQL, MongoDB · NUnit + Moq, integration test self-hosted"),
        ("Identity, storage e AI", "Keycloak con OAuth 2.0 · flussi JWT bearer · SeaweedFS tramite client compatibile S3 · inferenza LLM self-hosted con Ollama · pipeline RAG con ChromaDB e modelli di embedding · governance di Copilot e controllo della spesa AI"),
    ],
    "upstream": "Contributi upstream",
    "upstream_lead": "%d pull request su %d progetti che uso o da cui dipendo. %d già mergiate, %d ancora in review.",
    "merged": "Mergiate",
    "in_review": "In review",
    "in_review_count": "(%d pull request aperte)",
    "headers": ("Progetto", "Modifica", "PR"),
    "all_prs": "Tutte le pull request",
    "projects": "Progetti",
    "projects_headers": "| | Progetto | Cos'è | Stack | |\n|:-:|---|---|---|:-:|",
    "projects_rows": [
        ("kubectl-safe-rollout", "Plugin kubectl che spiega perché un rollout è fallito o si è bloccato. Classificazione deterministica, nessun LLM, e non scrive mai sul cluster", "`Go` `client-go`", "`v0.3.0`"),
        ("github-actions-recipes", "I workflow dietro ai miei post su CI/CD e FinOps, una variabile isolata per ricetta", "`GitHub Actions`", "`live`"),
        ("token-optimization", "Riduce il consumo di token quando lavori con agenti LLM. Rieseguire il setup non cambia nulla", "`PowerShell`", "`live`"),
    ],
    "krew_note": "`kubectl-safe-rollout` è [in submission su krew-index](https://github.com/kubernetes-sigs/krew-index/pull/6213), quindi sarà installabile con `kubectl krew install safe-rollout`.",
    "writing": "Scrivo",
    "writing_body": "Su LinkedIn scrivo dei dettagli di piattaforma che di solito nessuno verifica: come Azure DevOps risolve le sue tre sintassi di espressione, le regole di conformità per i runner self-hosted, cosa decide e cosa non decide la code review di Copilot, e se lo sconto di una reservation Azure si sta ancora applicando a qualcosa.",
    "read_linkedin": "Leggi su LinkedIn",
    "footer_cta": "Scrivimi",
    "badge_merged": "MERGIATE UPSTREAM",
    "badge_projects": "PROGETTI TOCCATI",
    "badge_plugin": "PLUGIN KUBECTL",
    "views": "VISITE AL PROFILO",
}


def render(t, prs, typing_lines):
    merged = ordered([p for p in prs if p["merged"]], MERGED_ORDER)
    openpr = ordered([p for p in prs if p["state"] == "open"], OPEN_ORDER)
    projects = len({p["repo"] for p in prs})
    div = '<img src="%s/assets/divider.svg" width="100%%" alt="" />' % RAW

    o = []
    o.append('<div align="center">\n')
    o.append('<img src="%s/assets/header.svg?v=2" width="100%%" alt="Gabriel Harnagea, DevOps and Platform Engineer" />\n' % RAW)
    o.append('<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=900&color=58A6FF&center=true&vCenter=true&width=760&lines=%s" alt="" />\n' % typing_lines)
    o.append('<br/>\n')
    o.append('<a href="https://www.linkedin.com/in/gabriel-harnagea/"><img src="%s/assets/pill-linkedin.svg?v=3" alt="LinkedIn" /></a>'
             '&nbsp;<a href="mailto:gabriel.harnagea06@gmail.com"><img src="%s/assets/pill-email.svg?v=3" alt="Email" /></a>'
             '&nbsp;<img src="%s/assets/pill-location-%s.svg?v=3" alt="%s" />\n'
             % (RAW, RAW, RAW, t["lang"], t["location"]))
    o.append('<br/>\n')
    o.append('<img src="%s/assets/stats-%s.svg?v=3" alt="" />\n' % (RAW, t["lang"]))
    o.append('<br/>\n')
    o.append(t["lang_note"] + "\n")
    o.append('</div>\n')
    o.append(div + "\n")

    o.append("## `▸` " + t["about"] + "\n")
    o.append(t["about_body"] + "\n")
    o.append("```yaml\n" + t["yaml"] + "\n```\n")
    o.append(div + "\n")

    o.append("## `▸` " + t["what"] + "\n")
    o.append("<table>\n<tr>")
    for slug, title, sub in t["cells"]:
        o.append('<td align="center" width="16.6%%"><img src="https://skillicons.dev/icons?i=%s&theme=dark" width="40" alt="" /><br/><b>%s</b><br/><sub>%s</sub></td>' % (slug, title, sub))
    o.append("</tr>\n</table>\n")
    o.append(div + "\n")

    o.append("## `▸` " + t["stack"] + "\n")
    o.append('<div align="center">\n')
    o.append('<img src="https://skillicons.dev/icons?i=azure,kubernetes,terraform,docker,githubactions,nginx,cs,dotnet,ts,react,nextjs,tailwind,go,rust,python,bash,powershell,postgres,mongodb,git&theme=dark&perline=10" alt="" />\n')
    o.append('</div>\n')
    o.append("<table>")
    for i, (title, body) in enumerate(t["stack_blocks"]):
        if i % 2 == 0:
            o.append("<tr>")
        o.append('<td width="50%" valign="top">\n')
        o.append("**" + title + "**  \n" + body + "\n")
        o.append("</td>")
        if i % 2 == 1:
            o.append("</tr>")
    o.append("</table>\n")
    o.append(div + "\n")

    o.append("## `▸` " + t["upstream"] + "\n")
    o.append(t["upstream_lead"] % (len(prs), projects, len(merged), len(openpr)) + "\n")
    o.append("**" + t["merged"] + "**\n")
    o.append(table(merged, t["headers"]) + "\n")
    o.append("<details>")
    o.append("<summary><b>%s</b> %s</summary>\n" % (t["in_review"], t["in_review_count"] % len(openpr)))
    o.append(table(openpr, t["headers"]) + "\n")
    o.append("</details>\n")
    o.append('<div align="center">\n')
    o.append('<a href="https://github.com/pulls?q=is%%3Apr+author%%3A%s"><img src="https://img.shields.io/badge/%s-1F6FEB?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="" /></a>\n' % (USER, t["all_prs"].replace(" ", "%20")))
    o.append('</div>\n')
    o.append(div + "\n")

    o.append("## `▸` " + t["projects"] + "\n")
    o.append(t["projects_headers"])
    for name, what, stack, status in t["projects_rows"]:
        o.append("| <img src=\"https://skillicons.dev/icons?i=%s&theme=dark\" width=\"20\" alt=\"\" /> | **[%s](https://github.com/%s/%s)** | %s | %s | %s |" % (
            {"kubectl-safe-rollout": "go", "github-actions-recipes": "githubactions",
             "token-optimization": "powershell"}[name], name, USER, name, what, stack, status))
    o.append("")
    o.append(t["krew_note"] + "\n")
    o.append(div + "\n")

    o.append("## `▸` " + t["writing"] + "\n")
    o.append(t["writing_body"] + "\n")
    o.append('<div align="center">\n')
    o.append('<a href="https://www.linkedin.com/in/gabriel-harnagea/"><img src="https://img.shields.io/badge/%s-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117" alt="" /></a>\n' % t["read_linkedin"].replace(" ", "%20"))
    o.append('</div>\n')

    o.append('<div align="center">\n')
    o.append('<img src="%s/assets/footer.svg?v=2" width="100%%" alt="" />\n' % RAW)
    o.append('<a href="mailto:gabriel.harnagea06@gmail.com"><img src="https://img.shields.io/badge/%s-1F6FEB?style=for-the-badge&logo=minutemailer&logoColor=white&labelColor=0D1117" alt="" /></a>' % t["footer_cta"].replace(" ", "%20"))
    o.append('<a href="https://www.linkedin.com/in/gabriel-harnagea/"><img src="%s/assets/pill-linkedin.svg?v=3" alt="LinkedIn" /></a>\n' % RAW)
    o.append('<br/>\n')
    o.append('<sub><img src="https://komarev.com/ghpvc/?username=%s&style=flat-square&color=1F6FEB&labelColor=10161F&label=%s" alt="" /></sub>\n' % (USER, t["views"].replace(" ", "+")))
    o.append('</div>')

    return "\n".join(o) + "\n"


TYPING_EN = ("DevOps+%26+Platform+Engineer;CI%2FCD+pipelines%2C+Helm+charts%2C+Terraform%2C+GitOps;"
             "FinOps+and+agentic+DevOps;Upstream+PRs+in+Kubernetes%2C+Docker%2C+.NET%2C+containerd")
TYPING_IT = ("DevOps+%26+Platform+Engineer;Pipeline+CI%2FCD%2C+Helm+chart%2C+Terraform%2C+GitOps;"
             "FinOps+e+agentic+DevOps;PR+upstream+su+Kubernetes%2C+Docker%2C+.NET%2C+containerd")


def main():
    prs = fetch_pull_requests()
    written = badges.write_all(
        ROOT, EN, IT,
        merged_count=len([p for p in prs if p["merged"]]),
        project_count=len({p["repo"] for p in prs}),
        plugin_version=PLUGIN_VERSION,
    )
    print("wrote %d badge assets" % len(written))
    for name, strings, typing in (("README.md", EN, TYPING_EN), ("README.it.md", IT, TYPING_IT)):
        path = os.path.join(ROOT, name)
        io.open(path, "w", encoding="utf-8", newline="\n").write(render(strings, prs, typing))
        print("wrote %s" % name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
