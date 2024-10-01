from sklearn.feature_selection import SelectKBest, f_classif

def feature_selection(X, y, k):
    # Select top k features based on ANOVA F-statistic
    selector = SelectKBest(score_func=f_classif, k=k)
    X_selected = selector.fit_transform(X, y)
    selected_features = selector.get_support(indices=True)

    return X_selected, selected_features
