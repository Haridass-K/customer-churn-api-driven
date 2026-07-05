from prefect.client.orchestration import get_client
import asyncio
import pandas as pd
import os
import matplotlib.pyplot as plt


async def main():
    async with get_client() as client:

        deployments = await client.read_deployments()

        deployment_records = []

        for deployment in deployments:
            deployment_records.append({
                "Application Detail": "Deployment",
                "Name": deployment.name,
                "ID": str(deployment.id),
                "Status / Type": "Available",
                "Additional Info": str(deployment.entrypoint)
            })

        work_pools = await client.read_work_pools()

        work_pool_records = []

        for pool in work_pools:
            work_pool_records.append({
                "Application Detail": "Work Pool",
                "Name": pool.name,
                "ID": str(pool.id),
                "Status / Type": str(pool.type),
                "Additional Info": str(pool.status)
            })

        flow_runs = await client.read_flow_runs(limit=5)

        flow_run_records = []

        for run in flow_runs:
            flow_run_records.append({
                "Application Detail": "Flow Run",
                "Name": run.name,
                "ID": str(run.id),
                "Status / Type": str(run.state_type),
                "Additional Info": str(run.start_time)
            })

        all_records = deployment_records + work_pool_records + flow_run_records

        df = pd.DataFrame(all_records)

        os.makedirs("reports", exist_ok=True)

        csv_output_path = "reports/prefect_api_application_details.csv"
        png_output_path = "reports/prefect_api_application_details.png"

        df.to_csv(csv_output_path, index=False)

        print("\nPrefect Built-in API Application Details")
        print(df)

        plt.figure(figsize=(14, 4))
        plt.axis("off")

        table = plt.table(
            cellText=df.values,
            colLabels=df.columns,
            loc="center"
        )

        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1.2, 1.5)

        plt.savefig(
            png_output_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(f"\nCSV saved successfully: {csv_output_path}")
        print(f"PNG saved successfully: {png_output_path}")


if __name__ == "__main__":
    asyncio.run(main())