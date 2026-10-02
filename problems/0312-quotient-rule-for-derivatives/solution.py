import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    def derivative(coeffs, a):
        if len(coeffs) <= 1: return 0
        power = len(coeffs) - 1
        curr_term = coeffs[0] * power
        return curr_term * (a ** (power-1)) + derivative(coeffs[1:], a)

    def subtitute(coeffs, a, curr_val = 0):
        if not coeffs:
            return curr_val
        next_val = curr_val * a + coeffs[0]
        return subtitute(coeffs[1:], a, next_val)

    result = (derivative(g_coeffs, x) * subtitute(h_coeffs, x, curr_val = 0) - derivative(h_coeffs, x) * subtitute(g_coeffs, x, curr_val = 0)) / subtitute(h_coeffs, x, curr_val = 0) ** 2

    return result 


    