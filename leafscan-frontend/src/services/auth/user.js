// src/services/auth/user.js
import { apiClient } from '../../lib/api';

export const userService = {
  async getCurrentUser() {
    return await apiClient.get(`/api/auth/me`);
  },

  async updateProfile(userData) {
    return await apiClient.put(`/api/auth/profile`, userData);
  },

  async getToken() {
    return localStorage.getItem('access_token');
  },

  isAuthenticated() {
    return !!localStorage.getItem('access_token');
  },
};

// For backward compatibility with components using getUserDetails
export const getUserDetails = async (userId) => {
  try {
    return await apiClient.get(`/api/auth/user/${userId}`);
  } catch (error) {
    console.error('Error fetching user details:', error);
    return null;
  }
};
