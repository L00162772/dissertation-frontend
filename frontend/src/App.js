import './App.css';
import Create from './components/create';
import Read from './components/read';
import Update from './components/update';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { AwsRum } from 'aws-rum-web';

try {
  const config = {
    sessionSampleRate: 1,
    guestRoleArn: "arn:aws:iam::751505345149:role/RUM-Monitor-us-east-1-751505345149-4082830924561-Unauth",
    identityPoolId: "us-east-1:4be0d68a-2a27-453a-b9cd-1ad5a7215a08",
    endpoint: "https://dataplane.rum.us-east-1.amazonaws.com",
    telemetries: ["performance","errors","http"],
    allowCookies: true,
    enableXRay: false
  };

  const APPLICATION_ID = '730c1a22-17cd-46e9-a419-c09c7ea1029c';
  const APPLICATION_VERSION = '1.0.0';
  const APPLICATION_REGION = 'us-east-1';

  const awsRum = new AwsRum(
    APPLICATION_ID,
    APPLICATION_VERSION,
    APPLICATION_REGION,
    config
  );
} catch (error) {
  console.log("An error has occured")
  console.log(error)
}


function App() {
  return (
    <Router>
      <div className="main">
        <h2 className="main-header">React User Tracking</h2>
        <div>
        <Routes>
          <Route exact path='/create' element={<Create />} />
          <Route exact path='/read' element={<Read />} />
          <Route path='/update' element={<Update />} />
          <Route exact path='/' element={<Create />} />
          </Routes>
        </div>
        <div style={{ marginTop: 20 }}>
          
        </div>

        
      </div>
    </Router>
  );
}

export default App;
