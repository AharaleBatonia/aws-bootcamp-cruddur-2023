import './ProfileInfo.css';
import {ReactComponent as ElipsesIcon} from './svg/elipses.svg';
import React from "react";

// [TODO] Authenication
// we are doing AWS Amplify implementation 
// adding AWS Amplify 
import { Auth } from 'aws-amplify';
// end of adding AWS Amplify 

export default function ProfileInfo(props) {
  const [popped, setPopped] = React.useState(false);

  const click_pop = (event) => {
    setPopped(!popped)
  }

  // adding AWS Amplify 
  
  const signOut = async () => {
    try {
        await Auth.signOut({ global: true });
        window.location.href = "/"
        console.log('signOut1')
      
        // adding cognito jwt token 
        localStorage.removeItem("access_token")
      
    } catch (error) {
        console.log('signOut2')
        console.log('error signing out: ', error);
    }
}
  
  // end of adding AWS Amplify 

  const classes = () => {
    let classes = ["profile-info-wrapper"];
    if (popped === true){
      classes.push('popped');
    }
    return classes.join(' ');
  }

  return (
    <div className={classes()}>
      <div className="profile-dialog">
        <button onClick={signOut}>Sign Out</button> 
      </div>
      <div className="profile-info" onClick={click_pop}>
        <div className="profile-avatar"></div>
        <div className="profile-desc">
          <div className="profile-display-name">{props.user.display_name || "My Name" }</div>
          <div className="profile-username">@{props.user.handle || "handle"}</div>
        </div>
        <ElipsesIcon className='icon' />
      </div>
    </div>
  )
}
