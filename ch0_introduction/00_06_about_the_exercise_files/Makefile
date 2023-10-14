# Makefile for linting using cfn-lint.

# Target: cfn-lint
# Description: This target runs cfn-lint to check the syntax and validity of a CloudFormation template.
#
# Prerequisites:
#   - cfn-lint: You must have cfn-lint installed on your system. Install it using pip:
#     ```
#     pip install cfn-lint
#     ```
#   - A CloudFormation template file named 'sample-application.yml' in the same directory as this Makefile.
#
# Usage: Run `make cfn-lint` to lint the CloudFormation template.
cfn-lint:
	cfn-lint -t ./sample-application.yml
