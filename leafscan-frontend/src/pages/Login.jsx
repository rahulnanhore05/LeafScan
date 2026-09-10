import React, { useState } from "react";
import logo from "../assets/leafScan.png";
import { Mail } from "lucide-react";
import FormField from "../components/ui/FormField";
import PasswordField from "../components/ui/PasswordField";
import FullWidthButton from "../components/ui/FullWidthButton";
import toast from "react-hot-toast";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setEmailError("");
    setPasswordError("");

    let valid = true;
    if (!email) {
      setEmailError("Email is required");
      valid = false;
    }

    if (!password) {
      setPasswordError("Password is required");
      valid = false;
    }

    if (!valid) return;

    setLoading(true);
    const result = await login(email, password);
    setLoading(false);

    if (!result.success) {
      toast.error("Login failed");
      setEmail("");
      setPassword("");
      return;
    }

    toast.success("Login successful!");
    navigate("/dashboard");
  };

  return (
    <div className="min-h-screen bg-[#f9fbf9] flex items-center justify-center px-4">
      <div className="bg-white rounded-2xl shadow-lg p-8 w-full max-w-md">
        {/* Header Section */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-full h-16 block px-[43%]">
            <img src={logo} alt="LeafScan Logo" className="w-12 h-12" />
          </div>
          <h1 className="text-2xl font-semibold text-green-700 mb-2">
            Welcome Back
          </h1>
          <p className="text-gray-600">Sign in to your LeafScan Account</p>
        </div>
        {/* Login Form */}
        <form onSubmit={handleSubmit}>
          <div className="space-y-6">
          <FormField
            htmlFor="email"
            label="Email Address"
            Icon={Mail}
            input_type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            error={emailError}
          />
          <PasswordField
            htmlFor="password"
            label="Password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            error={passwordError}
          />
            <FullWidthButton type="submit" body="Sign In" disabled={loading} />

          <div className="text-center pt-4">
            <span className="text-sm text-gray-600">
              Don't have an account?{" "}
            </span>
            <a
              href="/register"
              className="text-green-600 hover:text-green-700 font-medium"
            >
              Sign Up here
            </a>
          </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
