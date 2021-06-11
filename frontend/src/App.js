import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Login, Signup, UserDetail, UserEdit, UserList } from 'user/index'
import { Home, User, Counter, Item } from 'templetes'
import { Nav } from 'common'
import { BrowserRouter as Router} from 'react-router-dom'
import { todoReducer } from 'store'
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import { Schedule } from 'todos/containers'

const rootReducer = combineReducers({todoReducer})


const App = () => {
  return (<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>
        <Nav/>
    <Route exact path='/home' component={Home}/>
    <Redirect exact from={'/'} to={'./home'}/>
    <Route exact path='/counter' component={Counter}/>
    <Route exact path='/user' component={User}/>
    <Route exact path='/login-form' component={Login}/>
    <Route exact path='/signup-form' component={Signup}/>
    <Route exact path='/user-detail' component={UserDetail}/>
    <Route exact path='/user-modify' component={UserEdit}/>
    <Route exact path='/user-delete' component={UserList}/>
    <Route exact path='/item' component={Item}/>
    <Route exact path='/todos' component={Schedule}/>
      </Provider>
    </Router>
  </div>)

  
}

export default App