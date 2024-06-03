import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

# Parameters
num_faults = 11
num_features = 30
num_instances = 1000

# Generate synthetic data
np.random.seed(42)
X = np.random.randn(num_instances, num_features)
y = np.zeros(num_instances)
y[:num_faults] = 1  # Assign first `num_faults` instances as positive cases

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Manually oversample the minority class
num_copies = int((len(y_train) - np.sum(y_train)) // num_faults)
X_oversampled = np.vstack([X_train[y_train == 1]] * num_copies + [X_train[y_train == 0]])
y_oversampled = np.hstack([y_train[y_train == 1]] * num_copies + [y_train[y_train == 0]])

# Shuffle the oversampled data
indices = np.arange(len(y_oversampled))
np.random.shuffle(indices)
X_oversampled = X_oversampled[indices]
y_oversampled = y_oversampled[indices]

# Train a Logistic Regression model on the balanced dataset
model_oversampled = LogisticRegression()
model_oversampled.fit(X_oversampled, y_oversampled)

# Predict on test data with default threshold
y_pred_oversampled = model_oversampled.predict(X_test)

# Calculate precision
precision_oversampled = precision_score(y_test, y_pred_oversampled)

# Predict probabilities and adjust the threshold
y_prob_oversampled = model_oversampled.predict_proba(X_test)[:, 1]
threshold = 0.3
y_pred_oversampled_threshold = (y_prob_oversampled >= threshold).astype(int)
precision_oversampled_threshold = precision_score(y_test, y_pred_oversampled_threshold)

# Train a Logistic Regression model with class weights
model_weighted = LogisticRegression(class_weight='balanced')
model_weighted.fit(X_oversampled, y_oversampled)

# Predict on test data
y_pred_weighted = model_weighted.predict(X_test)
precision_weighted = precision_score(y_test, y_pred_weighted)

# Train a Random Forest model with class weights
model_rf = RandomForestClassifier(class_weight='balanced', random_state=42)
model_rf.fit(X_oversampled, y_oversampled)

# Predict on test data
y_pred_rf = model_rf.predict(X_test)
precision_rf = precision_score(y_test, y_pred_rf)

# Output the precision scores
print(f"Precision with oversampled Logistic Regression: {precision_oversampled}")
print(f"Precision with adjusted threshold Logistic Regression: {precision_oversampled_threshold}")
print(f"Precision with weighted Logistic Regression: {precision_weighted}")
print(f"Precision with Random Forest: {precision_rf}")

# Ensure some debugging information is printed
print(f"Number of positive instances in test set: {np.sum(y_test)}")
print(f"Number of positive predictions by Logistic Regression with oversampling: {np.sum(y_pred_oversampled)}")
print(f"Number of positive predictions by Logistic Regression with threshold adjustment: {np.sum(y_pred_oversampled_threshold)}")
print(f"Number of positive predictions by Logistic Regression with class weighting: {np.sum(y_pred_weighted)}")
print(f"Number of positive predictions by Random Forest: {np.sum(y_pred_rf)}")

