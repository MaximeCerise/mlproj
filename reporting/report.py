import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, ClassificationPreset


training_data = pd.read_csv("data/ref_data.csv")
production_data = pd.read_csv("data/prod_data.csv")
training_data.drop('embedding', axis=1, inplace=True)
production_data.drop('embedding', axis=1, inplace=True)


report = Report(metrics=[
    DataDriftPreset(),
    ClassificationPreset()
])


report.run(reference_data=training_data, current_data=production_data)


report.save_html("webapp/evidently_report.html")
print("Rapport Evidently généré : evidently_report.html")