# B22HS03 codes

There are two folders mainly that are divided into because we are having two
seperate models that is LayoutLMV2, Dessurt and a file which we used for
Data Visualization.

## LayoutLMV2

It has the ipynb files of the model

## Dessurt

It has the ipynb of the model, website code for which was made on top of the model.

For the website please go inside the website folder and run the following commands.

```sh
pip install -r requirements.txt
streamlit run main.py
```

The above commands will run the website and render it.

The Dessurt folder also has the results folder that is we trained the model and
tested the model on top of the validation dataset we got these csv files as output.
These are for checking accuracy, precision and recall for our model.
