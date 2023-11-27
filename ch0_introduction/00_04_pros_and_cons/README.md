# 00_04 Pros and Cons
Each CI/CD tool category has benefits and drawbacks.  Consider these factors when choosing a CI/CD tool category for your projects.

Regarding concerns about security vulnerabilities and vendor lock-in, expect these to be the same for all categories.

- **Self-Hosted CI/CD Tools**
  - Pros:
    - Offers maximum flexibility, allowing you to specify the entire technology stack, including software, hardware, and network.
    - Provides greater control over data flow, reducing concerns about data leaks.
  - Cons:
      - Requires maintenance and administration, which can be challenging alongside regular duties.
      - Scalability is limited to existing infrastructure.

- **Software as a Service (SaaS) CI/CD Tools**
  - Pros:
    - Easy to get started; No maintenance.
    - Many free or reasonably priced SaaS CI/CD services available.
    - Automatically create triggers from your repository.
  - Cons:
    - Costs can increase as team size increases or development rate grows.
    - Potential security concerns as data is on a system you don't control.

- **Cloud Service Providers**
  - Pros:
    - Easy integration with other services from the same provider.
    - Offers better control over project access using Identity and Access Management.
    - Has access to potentially unlimited resources.
  - Cons:
    - Setting up CI/CD pipelines can be more complex.
    - May lead to vendor lock-in, but this can be a concern in any CI/CD system.

- **Code Repository-Based CI/CD**
  - Pros:
    - Combines code repositories and CI/CD tools in one place.
    - Plenty of free or low-fee options for starting.
  - Cons:
    - Becomes expensive at larger scales.

[Next: 00_05 The Experimental Pipeline](../00_05_the_experimental_pipeline/README.md)

