import React, { useState } from "react";
import {
  Upload,
  Image as ImageIcon,
  CheckCircle,
  AlertCircle,
  Loader,
} from "lucide-react";
import DiagnosisLoader from "../loaders/DiagnosisLoader";

const ImageUploader = ({ onImageUpload, onPredictionResult }) => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const [error, setError] = useState(null);

  const BACKEND_URL = `http://localhost:8000/api/prediction/predict`;

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedImage(file);
      setPreviewUrl(URL.createObjectURL(file));
      setError(null);
      if (onImageUpload) {
        onImageUpload(true);
      }
    }
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0];
      setSelectedImage(file);
      setPreviewUrl(URL.createObjectURL(file));
      setError(null);
      if (onImageUpload) {
        onImageUpload(true);
      }
    }
  };

  const handleUpload = async () => {
    if (!selectedImage) {
      alert("Please select an image.");
      return;
    }

    setIsLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append("file", selectedImage);

    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch(BACKEND_URL, {
        method: "POST",
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => null);
        const errorMessage = errorData?.detail || errorData?.message || `Server error (${response.status})`;
        throw new Error(errorMessage);
      }

      const data = await response.json();
      
      if (onPredictionResult) {
        onPredictionResult(data);
      }

    } catch (error) {
      setError(`Failed to process image: ${error.message}`);
      setIsLoading(false);
    }
  };

  const handleAnalyzeClick = () => {
    handleUpload();
  };

  if (isLoading) {
    return <DiagnosisLoader />;
  }

  return (
    <div className="space-y-6">
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-2xl p-4">
          <div className="flex items-center space-x-3">
            <AlertCircle className="w-6 h-6 text-red-600 flex-shrink-0" />
            <div className="text-red-800">
              <p className="font-medium">Error occurred</p>
              <p className="text-sm mt-1">{error}</p>
            </div>
          </div>
        </div>
      )}

      <div
        className={`relative border-2 border-dashed rounded-2xl p-8 text-center transition-all duration-300 ${
          dragActive
            ? "border-green-400 bg-green-50"
            : previewUrl
            ? "border-green-300 bg-green-50/50"
            : "border-gray-300 hover:border-green-400 hover:bg-green-50/30"
        }`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          id="file-upload"
        />

        {!previewUrl ? (
          <div className="space-y-4">
            <div className="mx-auto w-16 h-16 bg-green-100 rounded-full flex items-center justify-center">
              <Upload className="w-8 h-8 text-green-600" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                Drop your image here, or{" "}
                <span className="text-green-600 hover:text-green-700 cursor-pointer underline">
                  browse
                </span>
              </h3>
              <p className="text-gray-500 text-sm">
                Supports: JPG, PNG, GIF up to 10MB
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            <div className="relative inline-block">
              <img
                src={previewUrl}
                alt="Preview"
                className="max-w-full max-h-64 rounded-lg shadow-lg object-cover"
              />
              <div className="absolute top-2 right-2 w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
                <CheckCircle className="w-5 h-5 text-white" />
              </div>
            </div>
            <p className="text-green-600 font-medium">
              Image uploaded successfully!
            </p>
            <button
              onClick={() => {
                setPreviewUrl(null);
                setSelectedImage(null);
                setError(null);
                if (onImageUpload) {
                  onImageUpload(false);
                }
              }}
              className="text-sm text-gray-500 hover:text-gray-700 underline"
            >
              Upload different image
            </button>
          </div>
        )}
      </div>

      {selectedImage && (
        <button
          onClick={handleAnalyzeClick}
          disabled={isLoading}
          className={`w-full py-4 px-6 rounded-xl font-semibold text-lg transition-all duration-300 flex items-center justify-center space-x-3 ${
            isLoading
              ? "bg-gray-400 cursor-not-allowed"
              : "bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
          } text-white`}
        >
          {isLoading ? (
            <>
              <Loader className="w-5 h-5 animate-spin" />
              <span>Analyzing...</span>
            </>
          ) : (
            <>
              <ImageIcon className="w-5 h-5" />
              <span>Analyze Plant Disease</span>
            </>
          )}
        </button>
      )}
    </div>
  );
};

export default ImageUploader;
