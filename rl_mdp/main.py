from util import create_mdp, create_policy_1, create_policy_2
from model_free_prediction.monte_carlo_evaluator import MCEvaluator

def main() -> None:
    """
    Starting point of the program, you can instantiate any classes, run methods/functions here as needed.
    """
    
    mdp = create_mdp()
    policy_1 = create_policy_1()
    policy_2 = create_policy_2()

    mc_evaluator = MCEvaluator(mdp)

    print(mc_evaluator.evaluate(policy_1, 1000))
    print(mc_evaluator.evaluate(policy_2, 1000))




if __name__ == "__main__":
    main()
