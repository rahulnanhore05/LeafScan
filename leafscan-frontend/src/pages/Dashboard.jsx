import {
  Camera,
  TrendingUp,
  Award,
  Target,
  Wind,
} from "lucide-react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import React, { useState, useEffect } from "react";
import heroImage from "../assets/dashboard.png";
import Image_Tomato from "../assets/Image_1.webp";
import Image_Vegitable from "../assets/Image_2.jpg";
import Image_Bell_pepper from "../assets/Bell_pepper.webp";
import Image_StrewBerry from "../assets/StrewBerry.jpg";


export default function Dashboard() {
  const { user } = useAuth();
  
  const username = user?.full_name || user?.username || user?.email?.split('@')[0] || "User";
  
  const [carouselIndex, setCarouselIndex] = useState(0);

  const carouselImages = [
    Image_Tomato,
    Image_Vegitable,
    Image_Bell_pepper,
    Image_StrewBerry,
  ];

  // Auto-rotate carousel every 5 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      setCarouselIndex((prev) => (prev + 1) % carouselImages.length);
    }, 5000);
    return () => clearInterval(interval);
  }, [carouselImages.length]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-green-50 to-green-100">
      <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxwYXRoIGQ9Ik0zNiAxOGMzLjMxNCAwIDYgMi42ODYgNiA2cy0yLjY4NiA2LTYgNi02LTIuNjg2LTYtNiAyLjY4Ni02IDYtNiIgc3Ryb2tlPSIjMTViNzFhIiBzdHJva2Utd2lkdGg9IjAuNSIgb3BhY2l0eT0iMC4xIi8+PC9nPjwvc3ZnPg==')] opacity-40"></div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="relative overflow-hidden rounded-3xl shadow-2xl mb-12 animate-fade-in">
          <div
            className="absolute inset-0 bg-cover bg-center"
            style={{ backgroundImage: `url(${heroImage})` }}
          >
            <div className="absolute inset-0 bg-gradient-to-r from-green-700/95 to-green-600/70" />
          </div>
          <div className="relative px-8 py-12 sm:px-12 sm:py-16">
            <div className="inline-flex items-center px-4 py-2 rounded-full bg-white/20 text-white border border-white/30 backdrop-blur-sm mb-4 text-sm font-medium hover:bg-white/30 transition-colors">
              Welcome Back
            </div>
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-4 animate-fade-in-up">
              Hello, {username}!
            </h1>
            <p
              className="text-lg sm:text-xl text-white/90 max-w-2xl animate-fade-in-up"
              style={{ animationDelay: "100ms" }}
            >
              Your plants are thriving! Let&apos;s continue monitoring their
              health together.
            </p>
          </div>
        </div>

        {/* Image Carousel and Stats Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-12">
          {/* Image Carousel */}
          <div className="lg:col-span-2">
            <div className="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl overflow-hidden border border-green-100/50 hover:shadow-2xl transition-all duration-300">
              <div className="relative w-full h-96">
                {carouselImages.map((image, index) => (
                  <img
                    key={index}
                    src={image}
                    alt={`Plant showcase ${index + 1}`}
                    className={`absolute inset-0 w-full h-full object-cover transition-opacity duration-1000 ${
                      index === carouselIndex ? "opacity-100" : "opacity-0"
                    }`}
                  />
                ))}
                <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
                
                <div className="absolute bottom-6 left-0 right-0 flex justify-center gap-2 px-4">
                  {carouselImages.map((_, index) => (
                    <button
                      key={index}
                      onClick={() => setCarouselIndex(index)}
                      className={`h-2 rounded-full transition-all ${
                        index === carouselIndex
                          ? "bg-white w-8"
                          : "bg-white/50 hover:bg-white/70 w-2"
                      }`}
                      aria-label={`Go to slide ${index + 1}`}
                    />
                  ))}
                </div>

                <div className="absolute bottom-6 left-6 bg-black/50 backdrop-blur-sm text-white px-4 py-2 rounded-full text-sm font-medium">
                  Featured Plants
                </div>
              </div>
            </div>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 gap-4">
            <div className="bg-gradient-to-br from-green-500 to-green-700 rounded-3xl shadow-xl p-6 text-white hover:shadow-2xl transition-all duration-300 hover:scale-[1.02]">
              <div className="flex items-center justify-between mb-2">
                <Target className="w-8 h-8 opacity-80" />
                <TrendingUp className="w-5 h-5" />
              </div>
              <div className="text-4xl font-bold mb-1">30+</div>
              <div className="text-white/90 font-medium">Categories</div>
            </div>

            <div className="bg-gradient-to-br from-blue-500 to-blue-700 rounded-3xl shadow-xl p-6 text-white hover:shadow-2xl transition-all duration-300 hover:scale-[1.02]">
              <div className="flex items-center justify-between mb-2">
                <Award className="w-8 h-8 opacity-80" />
                <TrendingUp className="w-5 h-5" />
              </div>
              <div className="text-4xl font-bold mb-1">99%</div>
              <div className="text-white/90 font-medium">Accuracy Rate</div>
            </div>
          </div>
        </div>

        {/* Main CTA Section - Diagnosis Focus */}
        <div className="bg-gradient-to-r from-green-700 via-green-600 to-emerald-600 rounded-3xl shadow-2xl p-8 sm:p-12 text-white animate-fade-in">
          <div className="max-w-3xl">
            <div className="flex items-center gap-3 mb-4">
              <Wind className="w-8 h-8 opacity-90" />
              <h2 className="text-3xl sm:text-4xl font-bold">
                Plant Disease Detection
              </h2>
            </div>
            <p className="text-lg text-green-100 mb-4 leading-relaxed">
              Get instant AI-powered diagnosis for your plants. Simply upload a photo
              of your plant's leaf or affected area, and our advanced machine learning
              model will identify any diseases, provide severity levels, and suggest
              comprehensive care treatments.
            </p>
            <p className="text-sm text-green-200 mb-6">
              ✓ Real-time diagnosis • ✓ Detailed care guidance • ✓ High accuracy rate
            </p>
            <Link to="/diagnosis">
              <button className="bg-white text-green-700 hover:bg-green-50 font-bold py-4 px-8 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105 flex items-center gap-3 text-lg">
                <Camera className="w-6 h-6" />
                Start Diagnosis
              </button>
            </Link>
          </div>
        </div>

        {/* Key Features Highlight */}
        <div className="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg p-6 border border-green-100/50 hover:shadow-xl transition-all duration-300">
            <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center mb-4">
              <Camera className="w-6 h-6 text-green-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              Quick Diagnosis
            </h3>
            <p className="text-gray-600 text-sm leading-relaxed">
              Upload any plant image and receive instant AI analysis within seconds. No expertise required.
            </p>
          </div>

          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg p-6 border border-blue-100/50 hover:shadow-xl transition-all duration-300">
            <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4">
              <Award className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              Highly Accurate
            </h3>
            <p className="text-gray-600 text-sm leading-relaxed">
              Trained on thousands of plant images with an 99% accuracy rate. Detect diseases early.
            </p>
          </div>

          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg p-6 border border-emerald-100/50 hover:shadow-xl transition-all duration-300">
            <div className="w-12 h-12 bg-emerald-100 rounded-xl flex items-center justify-center mb-4">
              <TrendingUp className="w-6 h-6 text-emerald-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              Care Guidance
            </h3>
            <p className="text-gray-600 text-sm leading-relaxed">
              Get detailed treatment recommendations and prevention tips tailored to your plant's condition.
            </p>
          </div>
        </div>
      </div>

      <style>{`
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(-10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fade-in {
          animation: fade-in 0.6s ease-out;
        }
        @keyframes fade-in-up {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fade-in-up {
          animation: fade-in-up 0.8s ease-out;
        }
      `}</style>
    </div>
  );
}
