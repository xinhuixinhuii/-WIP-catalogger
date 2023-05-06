import * as React from 'react';
// import { NavigationContainer } from '@react-navigation/native';
// import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from './tabs/home';
import CatListScreen from './tabs/catList';
import LoginScreen from './tabs/login';
import CatLogScreen from './tabs/catLogs';
import { Text } from 'react-native';

const App = () => {

  // const Tab = createBottomTabNavigator();

  return (
    <Text>it works!</Text>
    // <NavigationContainer>
    //   <Tab.Navigator>
    //     <Tab.Screen name="Home" component={HomeScreen} />
    //     <Tab.Screen name="Cat Logs" component={CatLogScreen} />
    //     <Tab.Screen name="Cat List" component={CatListScreen} />
    //     <Tab.Screen name="Login" component={LoginScreen} />
    //   </Tab.Navigator>
    // </NavigationContainer>
  );
};

export default App;