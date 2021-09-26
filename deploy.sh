echo "Initiating deployment..."
sam deploy --template-file template.yaml --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
