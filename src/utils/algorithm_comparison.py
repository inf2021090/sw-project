import streamlit as st

def compare_classifiers(knn_acc, dt_acc):
    # Check for overfitting (accuracy = 1.0)
    knn_overfit = knn_acc == 1.0
    dt_overfit = dt_acc == 1.0

    # Format output results
    if knn_acc > dt_acc:
        result = f"K-Nearest Neighbors (KNN) has better accuracy:\nKNN Accuracy = {knn_acc:.5f}, DT Accuracy = {dt_acc:.5f}"
    elif dt_acc > knn_acc:
        result = f"Decision Tree (DT) has better accuracy:\nDT Accuracy = {dt_acc:.5f}, KNN Accuracy = {knn_acc:.5f}"
    else:
        result = f"Both algorithms have the same accuracy:\nAccuracy = {knn_acc:.5f}"

    # Display warnings for potential overfitting
    if knn_overfit:
        st.warning("K-Nearest Neighbors (KNN) may be overfitting (Accuracy = 1.0)")
    if dt_overfit:
        st.warning("Decision Tree (DT) may be overfitting (Accuracy = 1.0)")

    return result

def compare_clusters(ari_km, ari_gmm):
    # Check for overfitting (ARI = 1.0)
    km_overfit = ari_km == 1.0
    gmm_overfit = ari_gmm == 1.0

    # Format output results
    if ari_km > ari_gmm:
        result = f"K-Means clustering has better Adjusted Rand Index (ARI):\nK-Means ARI = {ari_km:.5f}, GMM ARI = {ari_gmm:.5f}"
    elif ari_gmm > ari_km:
        result = f"Gaussian Mixture Model (GMM) has better Adjusted Rand Index (ARI):\nGMM ARI = {ari_gmm:.5f}, K-Means ARI = {ari_km:.5f}"
    else:
        result = f"Both algorithms have the same Adjusted Rand Index (ARI):\nARI = {ari_km:.5f}"

    # Display warnings for potential overfitting
    if km_overfit:
        st.warning("K-Means clustering may be overfitting (ARI = 1.0)")
    if gmm_overfit:
        st.warning("Gaussian Mixture Model (GMM) may be overfitting (ARI = 1.0)")

    return result
