This is a repository with automatic discourse annotation of Daily Dialog dataset. It contains 991 dialogs with each utterance segmented into sentences. Annotation was performed with the use of ChatGPT. Currently, `dd_annotation_results.tsv` contains 3 kinds of annotation:
- open goals annotation with no set classes. [Prompt](https://github.com/NikaSmilga/dialog_graphs/blob/main/prompts/open_goals.txt)
- annotation according to ([Goals-Plans-Action](https://en.wikipedia.org/wiki/Goals,_plans,_action_theory)) theory. [Prompt](https://github.com/NikaSmilga/dialog_graphs/blob/main/prompts/gpa_theory.txt)
- annotation according to ([DuRecDial 2.0](https://github.com/liuzeming01/DuRecDial) annotation scheme. In this case, we also attempted to track and annotated goal states (with little success, though). [Prompt](https://github.com/NikaSmilga/dialog_graphs/blob/main/prompts/durecdial_and_state.txt)

Other files contain analysis of the annotation results, specifically, open goals and DuRecDial-style goals.

With `dd_analysis.py`, you can see the goal-annotated dialogs in a user-friendly streamlit interface.

![Table with DuRecDial-style goal-annotated dialogs]<img width="1282" alt="Screenshot 2023-03-24 at 18 56 55" src="https://user-images.githubusercontent.com/42929200/227577449-55d6afcc-4e77-485d-ad04-f3a62ba1c454.png">

With `dd_visualisation.ipynb`, you can take a look at a larger-scale dataset analysis, with all annotated dialogs presented in graphs using networkx.
![One of the graphs for analysing DuRecDial-style goal-annotated dataset; dialogs that started with greeting]<img width="1086" alt="Screenshot 2023-03-24 at 18 59 48" src="https://user-images.githubusercontent.com/42929200/227578241-4f2ca6d3-9d28-4bd3-9bab-2ad5dd21f77b.png">
