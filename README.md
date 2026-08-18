<div align="center">

<img src="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/main/assets/header.svg" width="100%" alt="Gabriel Harnagea — DevOps &amp; Platform Engineer" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=900&color=58A6FF&center=true&vCenter=true&width=760&lines=DevOps+%26+Platform+Engineer+%C2%B7+Azure+%C2%B7+Kubernetes;CI%2FCD+pipelines%2C+Helm+charts%2C+Terraform%2C+GitOps;FinOps+%26+Agentic+DevOps;Upstream+PRs+to+Kubernetes%2C+Docker%2C+.NET%2C+containerd" alt="Typing SVG" />

<br/>

<a href="https://www.linkedin.com/in/gabriel-harnagea/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:gabriel.harnagea06@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
<img src="https://img.shields.io/badge/Turin,%20Italy-2C3E50?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Turin, Italy" />
<img src="https://komarev.com/ghpvc/?username=HarnageaGabriel&style=for-the-badge&color=58A6FF&label=PROFILE+VIEWS" alt="Profile views" />

</div>

---

### About

DevOps & Platform Engineer on enterprise projects — CI/CD, Kubernetes, Terraform and cloud cost.

I wrote the application code before I ran the infrastructure hosting it. It sounds like a detail, until a build breaks and someone has to know where to look.

Most of my open-source work starts the same way: something behaves wrong in a real deployment, I read the source, and the fix goes upstream instead of into a local patch.

```yaml
role:      DevOps & Platform Engineer
platform:  [Azure, Kubernetes, GitOps, Terraform, Azure DevOps, GitHub Actions]
also:      [FinOps, Agentic DevOps, .NET backend]
languages: [C#, TypeScript, Go, Rust, Python, Bash, PowerShell]
into:      [correctness bugs, observability gaps, release plumbing, cloud cost]
based_in:  Turin, Italy
```

---

### Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=azure,kubernetes,terraform,docker,githubactions,nginx,cs,dotnet,ts,react,nextjs,tailwind,go,rust,python,bash,powershell,postgres,mongodb,git&theme=dark&perline=10" alt="Tech stack" />

</div>

<table>
<tr>
<td width="50%" valign="top">

**Platform & CI/CD**
Azure DevOps YAML pipelines and reusable templates · GitHub Actions · Helm charts and Helmfile releases · OCI push to ACR/GHCR · ApiOps policy automation on Azure API Management · Jinja2 templating · branch policies, PR review, code review as a gate

</td>
<td width="50%" valign="top">

**Cloud & infrastructure**
Kubernetes on AKS and k3d on-prem · NGINX Ingress Controller · Terraform (azurerm, azuredevops) · VM Scale Sets as self-hosted agent pools · golden images for faster scale-out · Container Registry, Storage Accounts, Functions, Entra · reservation and cost governance

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Backend & architecture**
REST/HTTP APIs in .NET 8/9 · Worker Services · CQRS with MediatR · Domain-Driven Design · hexagonal and N-tier architectures · API gateway with Ocelot · EF Core and Dapper · PostgreSQL, MongoDB · NUnit + Moq, self-hosted integration tests

</td>
<td width="50%" valign="top">

**Identity, storage & AI**
Keycloak with OAuth 2.0 · JWT bearer flows · SeaweedFS through the S3-compatible client · self-hosted LLM inference with Ollama · RAG pipelines with ChromaDB and embedding models · Copilot governance and AI spend controls

</td>
</tr>
</table>

---

### Upstream contributions

Pull requests to projects I actually run or depend on.

| | Project | Change | PR |
|:-:|---|---|:-:|
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes/kube-openapi** | Fix duplicate map keys when a type embeds two structs sharing a field | [`#631`](https://github.com/kubernetes/kube-openapi/pull/631) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes-sigs/apiserver-network-proxy** | Add `connection_duration_seconds` histogram for post-dial connection lifespan | [`#899`](https://github.com/kubernetes-sigs/apiserver-network-proxy/pull/899) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes/perf-tests** | Unit tests for `clusterloader2/pkg/errors` | [`#4261`](https://github.com/kubernetes/perf-tests/pull/4261) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes/minikube** | VirtualBox: strip surrounding quotes before parsing `hostOnlyCIDR` | [`#23480`](https://github.com/kubernetes/minikube/pull/23480) |
| <img src="https://cdn.simpleicons.org/docker/2496ED" width="18"/> | **docker/cli** | Normalize registry server address to lowercase for credential lookup | [`#7184`](https://github.com/docker/cli/pull/7184) |
| <img src="https://cdn.simpleicons.org/containerd/575757" width="18"/> | **containerd/runwasi** | Gate `ctr image import --local` by detected `ctr` version | [`#1177`](https://github.com/containerd/runwasi/pull/1177) |
| <img src="https://cdn.simpleicons.org/argo/EF7B4D" width="18"/> | **argoproj/argo-workflows** | Scope `RemoveFromQueue` to the calling controller | [`#16739`](https://github.com/argoproj/argo-workflows/pull/16739) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **dotnet/runtime** | `CompareInfo.IsPrefix`/`IsSuffix` with `IgnoreSymbols` not ignoring leading/trailing symbols | [`#132397`](https://github.com/dotnet/runtime/pull/132397) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **dotnet/runtime** | Return empty string instead of throwing when `getpwuid_r` fails unexpectedly | [`#132396`](https://github.com/dotnet/runtime/pull/132396) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **dtolnay/cxx** | Strip `r#` prefix from raw identifiers in generated C++ names | [`#1749`](https://github.com/dtolnay/cxx/pull/1749) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **rust-embedded/heapless** | Add `shift_remove` family to `IndexMap`/`IndexSet` | [`#685`](https://github.com/rust-embedded/heapless/pull/685) |
| <img src="https://cdn.simpleicons.org/ansible/EE0000" width="18"/> | **ansible/terraform-provider-aap** | Remove `aap_host` from state on 404 during Read | [`#194`](https://github.com/ansible/terraform-provider-aap/pull/194) |
| <img src="https://cdn.simpleicons.org/microsoftazure/0078D4" width="18"/> | **Azure/azure-powershell** | Fix `Get-AzSubscription` silently ignoring mismatched `-TenantId` under MSI auth | [`#29994`](https://github.com/Azure/azure-powershell/pull/29994) |
| <img src="https://cdn.simpleicons.org/traefikproxy/24A1C1" width="18"/> | **traefik/traefik-helm-chart** | Restore `secretResourceNames` for namespaced Role | [`#1972`](https://github.com/traefik/traefik-helm-chart/pull/1972) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **nunit/nunit-console** | Fix `--list-extensions` showing the wrong target framework | [`#1861`](https://github.com/nunit/nunit-console/pull/1861) |
| <img src="https://cdn.simpleicons.org/nuget/004880" width="18"/> | **dotnet-outdated/dotnet-outdated** | Report packages whose source repo is archived or deleted | [`#781`](https://github.com/dotnet-outdated/dotnet-outdated/pull/781) |

<div align="center">

<a href="https://github.com/pulls?q=is%3Apr+author%3AHarnageaGabriel"><img src="https://img.shields.io/badge/See%20all%20pull%20requests-1F6FEB?style=for-the-badge&logo=github&logoColor=white" alt="All pull requests" /></a>

</div>

---

### Projects

<table>
<tr>
<td width="50%" valign="top">

**[github-actions-recipes](https://github.com/HarnageaGabriel/github-actions-recipes)** &nbsp;`YAML`

Runnable GitHub Actions workflows behind my CI/CD and FinOps write-ups — including the cache benchmark measured over 10 real runs on the same runner and dependency tree.

</td>
<td width="50%" valign="top">

**[token-optimization](https://github.com/HarnageaGabriel/token-optimization)** &nbsp;`PowerShell`

Tooling to cut token consumption in LLM-assisted development workflows — the practical side of keeping agentic DevOps affordable.

</td>
</tr>
</table>

---

### Writing

I publish on LinkedIn about the parts of the platform people take for granted: Azure DevOps expression evaluation, self-hosted runner compliance, GitHub Copilot governance, Azure reservation coverage, and what actually separates agentic DevOps from ordinary automation.

<div align="center">

<a href="https://www.linkedin.com/in/gabriel-harnagea/"><img src="https://img.shields.io/badge/Read%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Read on LinkedIn" /></a>

</div>

---

<div align="center">

### Contribution graph

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/output/github-snake.svg" />
  <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/output/github-snake.svg" />
</picture>

<img src="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/main/assets/footer.svg" width="100%" alt="" />

</div>
