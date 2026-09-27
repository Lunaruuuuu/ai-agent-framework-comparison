PRODUCT_DATA = [
    {
        "name": "Laptop Pro",
        "quantity": 5,
        "price": 1500
    },
    {
        "name": "Wireless Mouse",
        "quantity": 20,
        "price": 25
    },
    {
        "name": "Mechanical Keyboard",
        "quantity": 10,
        "price": 50
    }
]

SYSTEM_PROMPT = """
You are a sales data analyst.

Your task is to analyze the provided product sales data.

You MUST use the provided calculate_sales_metrics tool
to calculate the numerical sales metrics before writing the report.

After receiving the tool result:
1. State the total revenue.
2. State the total units sold.
3. State the average revenue per unit.
4. Identify the product with the highest revenue.
5. Provide a short business-oriented conclusion.

Do not manually calculate the numerical results when the tool is available.
Use the tool result as the source of truth.

Keep the final report concise and easy to understand.
"""

USER_PROMPT = f"""
Analyze the following product sales data:

{PRODUCT_DATA}

Use the calculate_sales_metrics tool and then create a concise sales report.
"""