import json
import time

from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

from common.scenario import PRODUCT_DATA, SYSTEM_PROMPT, USER_PROMPT


@tool("calculate_sales_metrics")
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
    role="Sales Data Analyst",

    goal="Analyze product sales data and produce an accurate report.",

    backstory=(
        "You are a sales data analyst who relies on "
        "calculation tools for numerical accuracy."
    ),

    system_template=SYSTEM_PROMPT,

    tools=[calculate_sales_metrics],

    llm=LLM(
        model="gemini/gemini-3.8-flash",
        temperature=0
    ),

    verbose=False,
    allow_delegation=False
)


task = Task(
    description=USER_PROMPT,

    expected_output=(
        "A concise sales analysis report containing "
        "the calculated metrics."
    ),

    agent=agent
)


crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=False
)


if __name__ == "__main__":
    start = time.perf_counter()

    result = crew.kickoff(
        inputs={
            "product_data": json.dumps(PRODUCT_DATA)
        }
    )

    latency = time.perf_counter() - start

    print("\n===== CREWAI RESULT =====")
    print(result)

    print(f"\nLatency: {latency:.2f} seconds")