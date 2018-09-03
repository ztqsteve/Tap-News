import React from 'react';
import Auth from '../Auth/Auth';

class Base extends React.Component {
    render(){
        return(
            <div>
              <nav className='nav-bar indigo lighten-1'>
                <div className='nav-wrapper'>
                  <a href='/' className='brand-logo'>&nbsp;&nbsp;Tap News</a>
                  <ul className='right' id='nav-mobile'>
                    {Auth.isUserAuthenticated() ?
                      (<div>
                          <li>{Auth.getEmail()}</li>
                          <li><a href='/logout'>Log out</a></li>
                       </div>)
                       :
                       (<div>
                           <li><a href='/login'>Log in</a></li>
                           <li><a href='/signup'>Sign up</a></li>
                        </div>)
                    }
                  </ul>
                </div>
              </nav>
              <br/>
              {this.props.children}
            </div>
        )
    }

}


export default Base;
