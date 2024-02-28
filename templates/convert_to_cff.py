import csv
import yaml
import re

# use delimiter '\t' for TSVs
def convert_to_cff(input_file_path, output_cff_file_path, delimiter=','):
    
    def read_file_content(input_file_path, delimiter):
        file_content = []
        with open(input_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            for row in reader:
                file_content.append(row)
        return file_content

    def build_cff(file_content):
        cff_data = {
            "cff-version": "1.2.0",
            "message": "If you use this software, please cite it as below.",
            "metadata": {
                "keywords": []
            },
            "references": []
        }

        stage_entry = None

        for entry in file_content:
            stage = entry.get("\ufeffStage") or entry.get("Stage")
            evaluation_name = entry.get("Evaluation name")
            metadata = entry.get("Metadata")
            self_assessed_score = entry.get("self-assessed score", "").strip()
            score_possible = entry.get("score possible", "").strip()

            if not stage and not evaluation_name and not metadata:
                continue

            if stage:
                stage_entry = {"Stage": stage, "Evaluations": []}
                cff_data["metadata"]["keywords"].append(stage_entry)

            if not stage_entry:
                stage_entry = {"Stage": "Unspecified Stage", "Evaluations": []}
                cff_data["metadata"]["keywords"].append(stage_entry)

            if evaluation_name:
                evaluation_entry = {
                    "Evaluation Name": evaluation_name,
                    **({"Metadata": metadata} if metadata else {}),
                    **({"self-assessed score": int(self_assessed_score)} if self_assessed_score.isdigit() else {}),
                    **({"score possible": int(score_possible)} if score_possible.isdigit() else {}),
                }
                stage_entry["Evaluations"].append(evaluation_entry)
            else:
                if metadata:
                    stage_entry["Metadata"] = metadata
                if self_assessed_score.isdigit():
                    stage_entry["self-assessed score"] = int(self_assessed_score)
                if score_possible.isdigit():
                    stage_entry["score possible"] = int(score_possible)

        return yaml.dump(cff_data, sort_keys=False, allow_unicode=True)

    def remove_empty_evaluations(yaml_content):
        # Remove lines with empty "Evaluations"
        return re.sub(r"Evaluations: \[\]\n(    )?", "", yaml_content)

    # Read the file content
    file_content = read_file_content(input_file_path, delimiter)
    
    # Convert the file content to .cff format
    cff_output = build_cff(file_content)

    # Remove lines with empty "Evaluations"
    cff_output_cleaned = remove_empty_evaluations(cff_output)

    # Write the cleaned .cff content to the specified output file
    with open(output_cff_file_path, 'w', encoding='utf-8') as cff_file:
        cff_file.write(cff_output_cleaned)
