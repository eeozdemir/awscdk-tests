import aws_cdk as core
import aws_cdk.assertions as assertions

from test_app.test_app_stack import TestAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_app/test_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestAppStack(app, "test-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
