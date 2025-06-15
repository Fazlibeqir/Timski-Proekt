# 🐝 Insect Classification using YOLOv8
A collaborative machine learning project comparing YOLOv8 classification models of different sizes for insect species recognition.

### 🎯 Project Objective
To evaluate and compare multiple YOLOv8 classification model variants (YOLOv8s-cls, YOLOv8m-cls, YOLOv8x-cls) in terms of accuracy, performance, and inference speed on a labeled insect image dataset.

## 📁 Dataset Preparation
The dataset was prepared by:

- Extracting and organizing insect images into labeled folders per class.

- Splitting into train/val/test subsets (80/10/10).

- Verifying image distribution and class balance.

- Final dataset structure:

```bash
  dataset/
├── train/
│   ├── Bombus_species1/
│   ├── Bombus_species2/
│   └── ...
├── val/
└── test/ 
```
Tools used:

- Python (Pandas, NumPy, shutil)

- Jupyter Notebooks(Anaconda and Colab) (fetch_data.ipynb)

## 🧠 Model Training
We trained three model variants using the Ultralytics YOLOv8 classification framework:

| Model Variant     | Notebook File               | Description                        |
|------------------|-----------------------------|------------------------------------|
| YOLOv8s-cls       | train_v1_baseline.ipynb     | Baseline (small) model              |
| YOLOv8m-cls + Aug | train_v2_augmented.ipynb    | medium model + data augmentation     |
| YOLOv8x-cls       | train_v3_bigger_model.ipynb | Extended capacity (extra-large)    |


Each training session includes:

- Custom training config

- Epoch logs

- Evaluation on validation/test sets

- Confusion matrix visualization
  
## 📊 Performance Comparison
| Model        | Accuracy (Top-1) | Inference Speed | Notes                                         |
|--------------|------------------|------------------|-----------------------------------------------|
| YOLOv8s-cls  | 43%              | ~5–10 ms/img     | Small model: fastest inference, decent accuracy |
| YOLOv8m+aug  | 70%              | ~10–15 ms/img    | Medium model with augmentation: balanced speed & improved accuracy |
| YOLOv8x-cls  | 74%              | ~20–25 ms/img    | Largest model: best accuracy, slowest inference |

- Detailed confusion matrices and classification reports included in test_and_eval.ipynb.

- Performance plots and metrics visualized in compare_all_versions.ipynb.


## 📈 Visual Results
- Confusion Matrix (per model)

- Precision / Recall / F1 Score reports

- Side-by-side performance plots

All generated in:

- test_and_eval.ipynb

- compare_all_versions.ipynb

## 📦 Final Deliverables
- 📁 Notebooks:

    - fetch_data.ipynb

    - train_v1_baseline.ipynb

    - train_v2_augmented.ipynb

    - train_v3_bigger_model.ipynb

    - test_and_eval.ipynb

    - compare_all_versions.ipynb

- Utils (We have them just in Google Drive, excluding common_funcs.py)
    - common_funcs.py
    - resultsV1.csv
    - resultsV2.csv
    - resultsV3.csv
    - bestV1.pt
    - bestV2.pt
    - bestV3.pt
    - 
## 🧾 Conclusion & Insights
- YOLOv8x-cls achieved the best classification accuracy (74%) but had the slowest inference time.

- YOLOv8s-cls was the fastest (~5–10ms/image) and is suitable for real-time applications with limited resources.

- YOLOv8m-cls with augmentation provided a strong balance between accuracy and speed.

- We learned the importance of augmentation, model scaling, and metric-driven evaluation in classification tasks.

## 🧑‍💻 Authors
- Беќир Фазли, 191045 (СИИС)

- Александар Тркалески, 216126 (КН)

- Ангела Бојкова, 216048 (КН)

- Јакуп Емини, 191036 (СИИС)

Course: Тимски Проект

Faculty: ФИНКИ – Факултет за компјутерски науки и инженерство
