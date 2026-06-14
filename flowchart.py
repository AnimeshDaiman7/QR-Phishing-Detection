from graphviz import Digraph

flow = Digraph()

flow.node('A', 'Start')
flow.node('B', 'Upload QR Code')
flow.node('C', 'Decode QR (OpenCV)')
flow.node('D', 'Extract URL')
flow.node('E', 'Handle Redirection')
flow.node('F', 'Feature Extraction')
flow.node('G', 'ML Model (Naive Bayes)')
flow.node('H', 'Prediction')
flow.node('I', 'Safe or Phishing')
flow.node('J', 'Display Result (UI)')
flow.node('K', 'End')

flow.edges(['AB','BC','CD','DE','EF','FG','GH','HI','IJ','JK'])

flow.render('qr_phishing_flowchart', format='png', view=True)