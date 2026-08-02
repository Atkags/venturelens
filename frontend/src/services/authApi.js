import API_URL from './apiClient';

export async function registerUser(userData){
  const response = await fetch(
    `${API_URL}/users/register/`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(userData),
    });

    const data = await response.json();
    
    if (!response.ok){
      throw new Error(data.detail || 'Registration failed');
    }

    return data;
}

export async function loginUser(credentials) {
  const response = await fetch(
    `${API_URL}/users/login/`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(credentials),
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || 'Login Failed');
  }

  return data;
}