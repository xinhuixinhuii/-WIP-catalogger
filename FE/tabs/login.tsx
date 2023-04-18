import * as React from 'react';
import { Alert, Button, Text, TextInput, View } from 'react-native';

const LoginScreen = () => {
  const [user, setUser] = React.useState<string>('')
  const [password, setPassword] = React.useState<string>('')

  const onLogin = () => Alert.alert(user, password)

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <TextInput 
        placeholder='Username'
        onChangeText={(user) => setUser(user)}
        style = {{borderWidth: 1, marginBottom: 10, paddingHorizontal: 10}}
      />
      <TextInput 
        placeholder='Password'
        onChangeText={(password) => setPassword(password)}
        style = {{borderWidth: 1, marginBottom: 10, paddingHorizontal: 10}}
        secureTextEntry = {true}
      />
      <Button 
        title='Login'
        onPress={onLogin}
      /> 
    </View>
  );
}

export default LoginScreen