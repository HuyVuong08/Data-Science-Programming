# Assignment #07: Cross Validation
## Reflection
- I've learned about the importance of cross-validation in evaluating machine learning models and how it helps to assess a model's generalization performance. By using cross-validation techniques like K-Fold Cross Validation, I can better understand how well a model performs on unseen data and avoid overfitting or underfitting. I've also gained insights into the benefits of using regularization techniques like Lasso, Ridge, and ElasticNet to improve model performance and prevent overfitting by penalizing complex models. Overall, this assignment has deepened my understanding of model evaluation and regularization methods, enhancing my ability to build more robust and reliable machine learning models.

- I learned lots of definitions and concepts in this assignment, e.g: RMSE, K-Fold Cross Validation, Bias-Variance Tradeoff, Overfitting, Underfitting, Regularization, residuals, and feature selection.

- I've learned the basic concept of residual analysis and checking for homoscedasticity, linearity, and normality of rsiduals.

- I've learned that in a plot of residuals versus predicted values if there’s a funnel shape it may indicate that a transformation of the data or a different model is needed.

- I learned about new models, e.g: Lasso, Ridge, and ElasticNet.

- We noticed that **Lasso** and **ElasticNet** appear to be the best-performing models based on Mean RMSE from cross-validation (`cross_val_score()`) and RMSE from `cross_val_predict()`. Their regularization may be preventing overfitting, allowing them to generalize better.
- Furthermore, **Linear Regression** and **Ridge Regression** show slightly higher RMSE values in cross-validation and lower RMSE on training data, indicating possible slight overfitting.

- Also, Lasso and ElasticNet are likely the best choices here, as they provide lower RMSE values consistently across cross-validation and do not show a significant increase in error when evaluated on new data.

## Reflection Questions

1. What do I believe I did well on this assignment?

- I believe I did well in implementing and comparing multiple regression models, specifically Linear Regression, Lasso, Ridge, and ElasticNet, to evaluate their performance on the forest fires dataset. Using 5-Fold Cross Validation allowed me to assess each model’s generalizability and identify the strengths and weaknesses of each technique.

2. What was the most challenging part of this assignment?

- The most challenging part was setting up and interpreting the different cross-validation functions—KFold, cross_val_predict(), and cross_val_score()—and understanding how each function operates and impacts model evaluation. I found it difficult to ensure consistency across these methods while keeping track of the metrics and predictions for comparative analysis. Understanding the regularization effects of Lasso, Ridge, and ElasticNet on feature selection and interpretation was also complex, particularly in determining the best regularization strength.

3. What would have made this assignment a better experience?

- A better experience would have included a guided explanation of the cross-validation functions and how each one differs in application, as well as practical examples of using regularization methods like Lasso, Ridge, and ElasticNet in a real-world context. More detailed documentation or examples on interpreting and tuning regularization parameters for these models would have made it easier to understand how to use each model effectively. Additionally, more insights on handling potential issues like overfitting when using regularization would have been helpful.

4. What do I need help with?

- I might need more help in understanding the models.
- I might need more help in dealing with overfitting and underfitting.