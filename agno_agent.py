import json
import time

from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.google import Gemini

from common.scenario import PRODUCT_DATA, SYSTEM_PROMPT, USER_PROMPT


def calculate_sales_metrics(product_data: str) -> str:
    """
    Calculate total revenue, total units, average revenue per unit,
    and identify the product with the highest revenue.

    Input must be a JSON string containing product sales data.
    """

    products = json.loads(product_data)

    total_revenue = 0
    total_units = 0
    highest_product = None
    highest_revenue = 0

    for product in products:
        revenue = product["quantity"] * product["price"]

        total_revenue += revenue
        total_units += product["quantity"]

        if revenue > highest_revenue:
            highest_revenue = revenue
            highest_product = product["name"]

    average_revenue = total_revenue / total_units

    return json.dumps({
        "total_revenue": total_revenue,
        "total_units": total_units,
        "average_revenue_per_unit": round(average_revenue, 2),
        "highest_revenue_product": highest_product,
        "highest_revenue": highest_revenue
    })


agent = Agent(
    model=Gemini(
        id="gemini-3.8-flash"
    ),
    tools=[calculate_sales_metrics],
    instructions=SYSTEM_PROMPT,
    markdown=True
)


if __name__ == "__main__":
    start = time.perf_counter()

    response = agent.run(
        USER_PROMPT
    )

    latency = time.perf_counter() - start

    print("\n===== AGNO RESULT =====")
    print(response.content)

    print(f"\nLatency: {latency:.2f} seconds")