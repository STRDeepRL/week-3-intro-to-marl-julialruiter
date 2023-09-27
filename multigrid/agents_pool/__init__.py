from multigrid.agents_pool.YourName_policies.YourPolicyName_policy_v2 import YourPolicyNameV2_Policy
from multigrid.agents_pool.YourName_policies.YourPolicyName_policy import YourPolicyName_Policy
from multigrid.agents_pool.YourName_policies.Custom_1_offensive import *
from multigrid.agents_pool.YourName_policies.Custom_2_goal import Custom_2_goal_Policy



SubmissionPolicies = {
    "your_policy_name": YourPolicyName_Policy,
    "your_policy_name_v2": YourPolicyNameV2_Policy,
    "Custom_1_BAD": Custom_1_offensive_Policy,
    "Custom_1_offensive": Custom_1_full_offensive_Policy,
    "Custom_2_goal": Custom_2_goal_Policy
}
