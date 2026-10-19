times = [1, 2, 3,]
actual = [12, 23, 37]

best_w = None
best_error = float("inf")

def predict_distances(times, w):
    predictions = []

    for time in times:
        predictions.append(float(time) * w)

    return predictions

def calculate_mae(actual, predicted):
    total_error = 0

    for measured, estimate in zip(actual, predicted):
        total_error += abs(measured - estimate)

    return (total_error / len(actual))

for w in range(8, 17):
    predicted = predict_distances(times, w)
    error = calculate_mae(actual, predicted)
    print(w, error)

    if error < best_error:
        best_error = error
        best_w = w

print("Best w:", best_w)
print("Best MAE:", best_error)

test_times = [4, 5]
test_actual = [49, 63]

test_predictions = predict_distances(test_times, best_w)
test_error = calculate_mae(test_actual, test_predictions)

print("Test predictions:", test_predictions)
print("Test MAE:", test_error)


