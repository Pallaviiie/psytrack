import api from "./api";

export interface RegisterData {
  full_name: string;
  email: string;
  password: string;
}

export interface LoginData {
  email: string;
  password: string;
}

export const registerUser = async (data: RegisterData) => {
  const response = await api.post("/users/register", data);
  return response.data;
};

export const loginUser = async (data: LoginData) => {
  const response = await api.post("/users/login", data);
  return response.data;
};
