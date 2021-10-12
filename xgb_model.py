from joblib import load

# sample tweet text
text = ["I want to die"]

# load the saved pipleine model
pipeline = load("suicide.joblib")

# predict on the sample tweet text
print(pipeline.predict(text))