import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, ClassificationPreset

# Charger les données
training_data = pd.read_csv("/Users/maximemoreau/Documents/ML/ML_deployement/MLproj/data/ref_data.csv")
production_data = pd.read_csv("/Users/maximemoreau/Documents/ML/ML_deployement/MLproj/data/prod_data.csv")

# Créer un rapport Evidently
report = Report(metrics=[
    DataDriftPreset(),
    ClassificationPreset()
])

# Générer le rapport
report.run(reference_data=training_data, current_data=production_data)

# Sauvegarder le rapport en HTML
report.save_html("ML_deployement/MLproj/reporting/performance_report.html")
print("Rapport généré : ML_deployement/MLproj/reporting/performance_report.html")