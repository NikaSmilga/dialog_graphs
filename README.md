This is a repository with automatic discourse annotation of Daily Dialog dataset. It contains 991 dialogs with each utterance segmented into sentences. Annotation was performed with the use of ChatGPT. Currently, `dd_annotation_results.tsv` contains 3 kinds of annotation:
- open goals annotation with no set classes. [Prompt](https://github.com/NikaSmilga/dialog_graphs/blob/main/prompts/open_goals.txt)
- annotation according to ([Goals-Plans-Action](https://en.wikipedia.org/wiki/Goals,_plans,_action_theory)) theory. [Prompt](https://github.com/NikaSmilga/dialog_graphs/blob/main/prompts/gpa_theory.txt)
- annotation according to ([DuRecDial 2.0](https://github.com/liuzeming01/DuRecDial)) annotation scheme. In this case, we also attempted to track and annotated goal states (with little success, though). [Prompt](https://github.com/NikaSmilga/dialog_graphs/blob/main/prompts/durecdial_and_state.txt)

Other files contain analysis of the annotation results, specifically, open goals and DuRecDial-style goals.

With `dd_analysis.py`, you can see the goal-annotated dialogs in a user-friendly streamlit interface.

<img width="1282" alt="Screenshot 2023-03-24 at 18 56 55" src="https://user-images.githubusercontent.com/42929200/227577449-55d6afcc-4e77-485d-ad04-f3a62ba1c454.png">

With `dd_visualisation.ipynb`, you can take a look at a larger-scale dataset analysis, with all annotated dialogs presented in graphs using networkx.

<img width="1095" alt="Screenshot 2023-03-24 at 19 02 54" src="https://user-images.githubusercontent.com/42929200/227579029-39b66909-5dcf-4598-8d15-10b368da8a63.png">

