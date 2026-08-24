<div align="center">

<img src="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/main/assets/header.svg?v=2" width="100%" alt="Gabriel Harnagea, DevOps and Platform Engineer" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=900&color=58A6FF&center=true&vCenter=true&width=760&lines=DevOps+%26+Platform+Engineer;CI%2FCD+pipelines%2C+Helm+charts%2C+Terraform%2C+GitOps;FinOps+and+agentic+DevOps;Upstream+PRs+in+Kubernetes%2C+Docker%2C+.NET%2C+containerd" alt="Typing SVG" />

<br/>

<a href="https://www.linkedin.com/in/gabriel-harnagea/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:gabriel.harnagea06@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
<img src="https://img.shields.io/badge/Turin,%20Italy-2C3E50?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Turin, Italy" />
<img src="https://komarev.com/ghpvc/?username=HarnageaGabriel&style=for-the-badge&color=58A6FF&label=PROFILE+VIEWS" alt="Profile views" />

</div>

---

### About

I'm a DevOps & Platform Engineer on enterprise projects: CI/CD, Kubernetes, Terraform, cloud cost.

I wrote application code before I ran the infrastructure that hosts it, which pays off mostly when a build breaks and someone has to know where to look.

The open-source work here comes from the same place. Something misbehaves in a real deployment, I go read the source, and the fix goes upstream rather than into a patch I keep to myself.

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

40 pull requests across 32 projects I run or depend on. 6 merged so far, 30 still in review.

**Merged**

| | Project | Change | PR |
|:-:|---|---|:-:|
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **dotnet/runtime** | Fix CompareInfo.IsPrefix/IsSuffix with CompareOptions.IgnoreSymbols not ignoring leading/trailing symbols | [`#132397`](https://github.com/dotnet/runtime/pull/132397) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes-sigs/apiserver-network-proxy** | Add connection_duration_seconds histogram for post-dial connection lifespan | [`#899`](https://github.com/kubernetes-sigs/apiserver-network-proxy/pull/899) |
| <img src="https://cdn.simpleicons.org/redis/FF4438" width="18"/> | **StackExchange/StackExchange.Redis** | Add NOMKSTREAM support to XADD | [`#3186`](https://github.com/StackExchange/StackExchange.Redis/pull/3186) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **DapperLib/DapperAOT** | Fix false-positive DAP214 for {=XXX} literal-replacement syntax | [`#191`](https://github.com/DapperLib/DapperAOT/pull/191) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **nunit/nunit-console** | Add AssemblyTargetFramework to IExtensionNode | [`#1867`](https://github.com/nunit/nunit-console/pull/1867) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **nunit/nunit-console** | Fix --list-extensions showing wrong target framework for extensions | [`#1861`](https://github.com/nunit/nunit-console/pull/1861) |

<details>
<summary><b>In review</b> (30 open pull requests)</summary>

| | Project | Change | PR |
|:-:|---|---|:-:|
| <img src="https://cdn.simpleicons.org/docker/2496ED" width="18"/> | **moby/moby** | C8d/resolver: reuse per-host authorizers across a pull | [`#53457`](https://github.com/moby/moby/pull/53457) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes/kube-openapi** | Fix duplicate map keys when a type embeds two structs sharing a field | [`#631`](https://github.com/kubernetes/kube-openapi/pull/631) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes-sigs/krew-index** | Add safe-rollout plugin | [`#6213`](https://github.com/kubernetes-sigs/krew-index/pull/6213) |
| <img src="https://cdn.simpleicons.org/kubernetes/326CE5" width="18"/> | **kubernetes/perf-tests** | Add unit tests for pkg/errors | [`#4261`](https://github.com/kubernetes/perf-tests/pull/4261) |
| <img src="https://cdn.simpleicons.org/docker/2496ED" width="18"/> | **docker/cli** | Registry: normalize server address to lowercase for credential lookup | [`#7184`](https://github.com/docker/cli/pull/7184) |
| <img src="https://cdn.simpleicons.org/containerd/575757" width="18"/> | **containerd/runwasi** | Gate ctr image import --local by detected ctr version | [`#1177`](https://github.com/containerd/runwasi/pull/1177) |
| <img src="https://cdn.simpleicons.org/argo/EF7B4D" width="18"/> | **argoproj/argo-cd** | Add ignoreDraft filter to ApplicationSet Pull Request generator | [`#29265`](https://github.com/argoproj/argo-cd/pull/29265) |
| <img src="https://cdn.simpleicons.org/argo/EF7B4D" width="18"/> | **argoproj/argo-rollouts** | Stop degraded stable RS from permanently blocking subset DestinationRule switch | [`#4990`](https://github.com/argoproj/argo-rollouts/pull/4990) |
| <img src="https://cdn.simpleicons.org/argo/EF7B4D" width="18"/> | **argoproj/argo-workflows** | Scope RemoveFromQueue to the calling controller | [`#16739`](https://github.com/argoproj/argo-workflows/pull/16739) |
| <img src="https://cdn.simpleicons.org/cncf/231F20" width="18"/> | **open-policy-agent/opa** | Make allow_net restrict file:// refs in JSON schemas | [`#9044`](https://github.com/open-policy-agent/opa/pull/9044) |
| <img src="https://cdn.simpleicons.org/cncf/231F20" width="18"/> | **spiffe/spire** | Fix inaccurate expiring/outdated SVID sync metrics | [`#7230`](https://github.com/spiffe/spire/pull/7230) |
| <img src="https://cdn.simpleicons.org/thanos/6D49FF" width="18"/> | **thanos-io/objstore** | Gcs: support custom GCS API endpoint via endpoint config option | [`#270`](https://github.com/thanos-io/objstore/pull/270) |
| <img src="https://cdn.simpleicons.org/saltproject/57BCAD" width="18"/> | **saltstack/salt** | Fix file.managed omitting mode from changes when creating a file | [`#70084`](https://github.com/saltstack/salt/pull/70084) |
| <img src="https://cdn.simpleicons.org/saltproject/57BCAD" width="18"/> | **saltstack/salt** | Fix module.run: positional arg for defaulted param raises 'multiple values' | [`#70083`](https://github.com/saltstack/salt/pull/70083) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **BurntSushi/ripgrep** | Search-zip: detect compressed files by magic number, not just extension | [`#3516`](https://github.com/BurntSushi/ripgrep/pull/3516) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **BurntSushi/ripgrep** | Ignore: fix dangling backslash error for escaped trailing space with extra spaces | [`#3515`](https://github.com/BurntSushi/ripgrep/pull/3515) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **tokio-rs/tracing** | Subscriber: add opt-in field value truncation wrapper | [`#3600`](https://github.com/tokio-rs/tracing/pull/3600) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **dtolnay/cxx** | Strip r# prefix from raw identifiers in generated C++ names | [`#1749`](https://github.com/dtolnay/cxx/pull/1749) |
| <img src="https://cdn.simpleicons.org/rust/DEA584" width="18"/> | **rust-embedded/heapless** | Add shift_remove family to IndexMap/IndexSet | [`#685`](https://github.com/rust-embedded/heapless/pull/685) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **dotnet/runtime** | Return empty string instead of throwing when getpwuid_r fails unexpectedly | [`#132396`](https://github.com/dotnet/runtime/pull/132396) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **dotnet/msbuild** | Disable nullable analysis for net4x leg of multi-targeted projects | [`#14738`](https://github.com/dotnet/msbuild/pull/14738) |
| <img src="https://cdn.simpleicons.org/redis/FF4438" width="18"/> | **StackExchange/StackExchange.Redis** | Fix Sentinel connection leak and AbortOnConnectFail=false handling | [`#3187`](https://github.com/StackExchange/StackExchange.Redis/pull/3187) |
| <img src="https://cdn.simpleicons.org/redis/FF4438" width="18"/> | **StackExchange/StackExchange.Redis** | Make fallback discovery and keep-alive probes cluster-slot aware | [`#3185`](https://github.com/StackExchange/StackExchange.Redis/pull/3185) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **quartznet/quartznet** | Add job type exclusion filter to trigger acquisition | [`#3282`](https://github.com/quartznet/quartznet/pull/3282) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **NLog/NLog** | DateLayoutRenderer - Changed default Format to yyyy-MM-dd HH:mm:ss.ffff | [`#6252`](https://github.com/NLog/NLog/pull/6252) |
| <img src="https://cdn.simpleicons.org/dotnet/512BD4" width="18"/> | **nsubstitute/NSubstitute** | Document that Received.InOrder does not track property getters | [`#998`](https://github.com/nsubstitute/NSubstitute/pull/998) |
| <img src="https://cdn.simpleicons.org/nuget/004880" width="18"/> | **dotnet-outdated/dotnet-outdated** | Report packages whose source repo is archived or deleted (GitHub only) | [`#781`](https://github.com/dotnet-outdated/dotnet-outdated/pull/781) |
| <img src="https://cdn.simpleicons.org/ansible/EE0000" width="18"/> | **ansible/terraform-provider-aap** | Remove aap_host from state on 404 during Read | [`#194`](https://github.com/ansible/terraform-provider-aap/pull/194) |
| <img src="https://cdn.simpleicons.org/traefikproxy/24A1C1" width="18"/> | **traefik/traefik-helm-chart** | Restore secretResourceNames for namespaced Role | [`#1972`](https://github.com/traefik/traefik-helm-chart/pull/1972) |
|  | **Azure/azure-powershell** | Fix Get-AzSubscription silently ignoring mismatched -TenantId under MSI auth | [`#29994`](https://github.com/Azure/azure-powershell/pull/29994) |

</details>

<div align="center">

<a href="https://github.com/pulls?q=is%3Apr+author%3AHarnageaGabriel"><img src="https://img.shields.io/badge/See%20all%20pull%20requests-1F6FEB?style=for-the-badge&logo=github&logoColor=white" alt="All pull requests" /></a>

</div>

---

### Projects

<table>
<tr>
<td width="50%" valign="top">

**[kubectl-safe-rollout](https://github.com/HarnageaGabriel/kubectl-safe-rollout)** &nbsp;`Go` &nbsp;`Apache-2.0`

A kubectl plugin that tells you why a rollout failed or stalled. The cause classification is deterministic, there is no LLM in it, and it never writes to the cluster. Currently at v0.3.0, with the plugin submitted to [krew-index](https://github.com/kubernetes-sigs/krew-index/pull/6213).

</td>
<td width="50%" valign="top">

**[github-actions-recipes](https://github.com/HarnageaGabriel/github-actions-recipes)** &nbsp;`YAML`

The workflows behind my CI/CD and FinOps posts, including the caching benchmark I ran 10 times on one runner.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[token-optimization](https://github.com/HarnageaGabriel/token-optimization)** &nbsp;`PowerShell`

Cuts token usage when you work with LLM coding agents. Setup is idempotent, so re-running it is safe.

</td>
<td width="50%" valign="top">
&nbsp;
</td>
</tr>
</table>

---

### Writing

I write on LinkedIn about platform details that usually pass unchecked: how Azure DevOps resolves its three expression syntaxes, the compliance rules for self-hosted runners, what Copilot code review does and does not decide, and whether an Azure reservation discount is still applying to anything.

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

<img src="https://raw.githubusercontent.com/HarnageaGabriel/HarnageaGabriel/main/assets/footer.svg?v=2" width="100%" alt="" />

</div>
