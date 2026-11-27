# Finance reconciliation: join grain

Illustrative values only: project P1 has two finance rows (100 and 150) and three task rows. Joining both detail tables directly on project ID produces six rows and incorrectly sums finance to 750 rather than 250.

Aggregate finance by project before joining it to project-level task summaries. Check that total cost before and after the join remains 250. Apply consistent period filters to the source records before aggregation. This example is instructional, not a result from the shipped dataset.
