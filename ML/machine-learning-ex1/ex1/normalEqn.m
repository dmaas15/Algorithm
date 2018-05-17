function [theta] = normalEqn(X, y)
%NORMALEQN Computes the closed-form solution to linear regression 
%   NORMALEQN(X,y) computes the closed-form solution to linear 
%   regression using the normal equations.

theta = zeros(size(X, 2), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the code to compute the closed form solution
%               to linear regression and put the result in theta.
%

% ---------------------- Sample Solution ----------------------

%normX=featureNormalize(X(:,2:3));
m = length(y);
%X = [ones(m, 1) normX];

%theta=(transpose(normX)*normX)^-1*transpose(normX)*y;
theta=((transpose(X)*X)^-1)*transpose(X)*y;


% -------------------------------------------------------------


% ============================================================

end
