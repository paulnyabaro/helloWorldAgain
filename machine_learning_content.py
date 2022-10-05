# Machine learning is a branch of artificial intelligence and is based on
# building models by learning pattern from data and using those models to make prediction

# Libraries for machine learning
# NumPy, pandas, SciPy, scikit-learn, and PySpark

#iris_save_load_predict_model.py
#model is creating using the code in #iris_build_svm_model.py
#saving the model to a file
# with open("model.pkl", 'wb') as file:
# pickle.dump(model, file)
# #loading the model from a file (in another application
# with open("model.pkl", 'rb') as file:
#     loaded_model = pickle.load(file)
#     x_new = [[5.6, 2.6, 3.9, 1.2]]
#     y_new = loaded_model.predict(x_new)
#     print("X=%s, Predicted=%s" % (x_new[0], y_new[0]))