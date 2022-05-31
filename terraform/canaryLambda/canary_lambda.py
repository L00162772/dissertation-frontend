from cgi import test


def lambda_handler(event, context):
    print(f"event:{event}")

    test_run_status = event['detail']['test-run-status']
    print(f"test_run_status:{test_run_status}")
   
    if test_run_status.lower() == "failed":
        print("Test failed - remove region from global accelerator")
    else:
        print("Test Passed - verify region is part of global accelerator")
 