# utils/algorithm_comparison.py

import streamlit as st

def compare_algorithms(knn_metrics, svm_metrics, knn_metrics_selected=None, svm_metrics_selected=None):
    """
    Compare KNN and SVM metrics and highlight the better performing model.
    Arguments:
        knn_metrics: Tuple of (accuracy, f1_score, roc_auc) for KNN on original data
        svm_metrics: Tuple of (accuracy, f1_score, roc_auc) for SVM on original data
        knn_metrics_selected: Tuple of (accuracy, f1_score, roc_auc) for KNN on reduced data (optional)
        svm_metrics_selected: Tuple of (accuracy, f1_score, roc_auc) for SVM on reduced data (optional)
    """

    def highlight_better_metric(metric1, metric2, metric_name, label1, label2):
        if metric1 is None and metric2 is None:
            return f"No {metric_name} available."
        elif metric1 is None:
            return f"{label2} performs better on {metric_name}."
        elif metric2 is None:
            return f"{label1} performs better on {metric_name}."
        elif metric1 > metric2:
            return f"{label1} performs better on {metric_name}."
        elif metric1 < metric2:
            return f"{label2} performs better on {metric_name}."
        else:
            return f"Both {label1} and {label2} perform equally on {metric_name}."

    #  KNN vs SVM on Original Data
    st.write("### Comparing KNN and SVM on Original Data")
    accuracy_knn, f1_knn, roc_auc_knn = knn_metrics
    accuracy_svm, f1_svm, roc_auc_svm = svm_metrics

    st.write(highlight_better_metric(accuracy_knn, accuracy_svm, "Accuracy", "KNN (Original)", "SVM (Original)"))
    st.write(highlight_better_metric(f1_knn, f1_svm, "F1 Score", "KNN (Original)", "SVM (Original)"))
    st.write(highlight_better_metric(roc_auc_knn, roc_auc_svm, "ROC-AUC", "KNN (Original)", "SVM (Original)"))

    # Compare on reduced data if available
    if knn_metrics_selected and svm_metrics_selected:
        st.write("### Comparing KNN and SVM on Reduced Data")
        accuracy_knn_selected, f1_knn_selected, roc_auc_knn_selected = knn_metrics_selected
        accuracy_svm_selected, f1_svm_selected, roc_auc_svm_selected = svm_metrics_selected

        st.write(highlight_better_metric(accuracy_knn_selected, accuracy_svm_selected, "Accuracy", "KNN (Reduced)", "SVM (Reduced)"))
        st.write(highlight_better_metric(f1_knn_selected, f1_svm_selected, "F1 Score", "KNN (Reduced)", "SVM (Reduced)"))
        st.write(highlight_better_metric(roc_auc_knn_selected, roc_auc_svm_selected, "ROC-AUC", "KNN (Reduced)", "SVM (Reduced)"))

    #  Original vs Reduced for KNN
    if knn_metrics_selected:
        st.write("### KNN: Original vs Reduced Data Comparison")
        st.write(highlight_better_metric(accuracy_knn, accuracy_knn_selected, "Accuracy", "KNN (Original)", "KNN (Reduced)"))
        st.write(highlight_better_metric(f1_knn, f1_knn_selected, "F1 Score", "KNN (Original)", "KNN (Reduced)"))
        st.write(highlight_better_metric(roc_auc_knn, roc_auc_knn_selected, "ROC-AUC", "KNN (Original)", "KNN (Reduced)"))

    #  Original vs Reduced for SVM
    if svm_metrics_selected:
        st.write("### SVM: Original vs Reduced Data Comparison")
        st.write(highlight_better_metric(accuracy_svm, accuracy_svm_selected, "Accuracy", "SVM (Original)", "SVM (Reduced)"))
        st.write(highlight_better_metric(f1_svm, f1_svm_selected, "F1 Score", "SVM (Original)", "SVM (Reduced)"))
        st.write(highlight_better_metric(roc_auc_svm, roc_auc_svm_selected, "ROC-AUC", "SVM (Original)", "SVM (Reduced)"))
