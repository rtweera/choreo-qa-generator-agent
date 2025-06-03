Here is one question and answer based on the provided documentation excerpt on Choreo concepts:

1.  **Question:** My company is evaluating setting up a private data plane instead of using the cloud data plane due to strict data residency and privacy requirements. What are the fundamental infrastructure requirements for a private data plane, what key system components are typically installed via Helm during setup, and importantly, how does the platform ensure that our application logs and observability data remain within our private infrastructure while still being accessible through the console?

    **Answer:** Setting up a private data plane addresses strict data requirements by providing dedicated infrastructure for your organization. The fundamental infrastructure requirements typically include:

    *   Upstream-compatible Kubernetes clusters.
    *   A container registry.
    *   A key vault (secret store).
    *   A logging service or log storage.

    During setup, a Helm installation on your Kubernetes infrastructure deploys core system components such as Cilium CNI and service mesh, API Gateways and related components, the PDP agent, Observability and logging APIs with agents, and the Flux controller. These components are automatically updated via the Flux controller connected to the platform's Update Management System.

    Regarding logs and observability, the architecture is designed with data privacy in mind. Logs and observability data are stored directly within the data plane itself. When you view this data through the platform's console, your browser establishes a direct interaction with APIs located within your data plane to fetch the necessary information. This direct browser-to-data-plane interaction minimizes data transfer points, ensures sensitive data remains within your private infrastructure, and aligns with data locality requirements while still providing you with the necessary insights via the console.