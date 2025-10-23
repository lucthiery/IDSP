from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    precision_recall_curve,
    f1_score,
    accuracy_score
)
import numpy as np
import matplotlib.pyplot as plt


def evaluate_model(y_true, y_pred_proba):
    # --- Core metrics ---
    roc = roc_auc_score(y_true, y_pred_proba)
    pr = average_precision_score(y_true, y_pred_proba)

    # --- Best F1 threshold ---
    prec, rec, thr = precision_recall_curve(y_true, y_pred_proba)
    f1s = (2 * prec * rec) / (prec + rec + 1e-12)
    best_idx = np.nanargmax(f1s)
    best_thr = thr[max(best_idx - 1, 0)] if best_idx < len(thr) else 0.5

    # --- Predictions and final scores ---
    y_pred = (y_pred_proba >= best_thr).astype(int)
    f1 = f1_score(y_true, y_pred)
    acc = accuracy_score(y_true, y_pred)

    # --- Print summary ---
    print(f"ROC-AUC: {roc:.4f} | PR-AUC: {pr:.4f} | "
          f"F1@{best_thr:.3f}: {f1:.4f} | ACC: {acc:.4f}")

    # --- Return as dict ---
    return {
        "ROC-AUC": roc,
        "PR-AUC": pr,
        "f1s": f1s,
        "F1": f1,
        "ACC": acc,
        "thr": thr,
        "best_thr": best_thr,
        "y_pred":y_pred
    }

def plot_threshold(threshold, best_thr, f1s):
    plt.plot(threshold, f1s[:-1])
    plt.axvline(best_thr, color='r', linestyle='--')
    plt.xlabel("Threshold")
    plt.ylabel("F1 Score")
    plt.title(f"Best Threshold = {best_thr:.3f}")
    plt.show()

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
def plot_confusion(y_test, y_pred, best_thr):
    cm = confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Bot", "Human"]
    )
    disp.plot(cmap="Blues", values_format=",.0f")
    plt.title(f"Confusion Matrix (Threshold={best_thr:.3f})")
    plt.show()

    # Optional: print numeric values
    tn, fp, fn, tp = cm.ravel()
    print(f"True Negatives: {tn}\nFalse Positives: {fp}\nFalse Negatives: {fn}\nTrue Positives: {tp}")
