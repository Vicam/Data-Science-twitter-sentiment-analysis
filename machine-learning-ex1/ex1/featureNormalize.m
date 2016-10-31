function [X_norm, mu, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normalizes the features in X 
%   FEATURENORMALIZE(X) returns a normalized version of X where
%   the mean value of each feature is 0 and the standard deviation
%   is 1. This is often a good preprocessing step to do when
%   working with learning algorithms.

% You need to set these values correctly
X_norm = X;
numberVariable = size(X, 2);
mu = zeros(1, numberVariable);
sigma = ones(1, numberVariable);

% ====================== YOUR CODE HERE ======================
% Instructions: First, for each feature dimension, compute the mean
%               of the feature and subtract it from the dataset,
%               storing the mean value in mu. Next, compute the 
%               standard deviation of each feature and divide
%               each feature by it's standard deviation, storing
%               the standard deviation in sigma. 
%
%               Note that X is a matrix where each column is a 
%               feature and each row is an example. You need 
%               to perform the normalization separately for 
%               each feature. 
%
% Hint: You might find the 'mean' and 'std' functions useful.
%       
for variable = 1:numberVariable
	mu(1,variable) = mean(X(:, variable));
	sigma(1, variable) = std(X(:, variable));  %std standard deviation alternative method of range
%	if (sigma(1, variable) ==0)
%		sigma(1, variable) = 1;
%	end
	X_norm(:,variable) = (X_norm(:,variable)-mu(1,variable))/sigma(1, variable);
end








% ============================================================

end
