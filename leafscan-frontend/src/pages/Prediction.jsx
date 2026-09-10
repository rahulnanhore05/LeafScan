import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { AlertTriangle, Lightbulb, Leaf, Bug, Wind } from "lucide-react";
import CareAdviceItem from "../components/ui/CareAdviceItem";
import DiagnosisLoader from "../components/loaders/DiagnosisLoader";
import { motion } from "framer-motion";

const Prediction = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let predictionData = location.state?.predictionData;

    if (!predictionData) {
      const storedData = sessionStorage.getItem("predictionResult");
      if (storedData) {
        try {
          predictionData = JSON.parse(storedData);
        } catch (error) {
        }
      }
    }

    if (predictionData) {

      const transformedCareAdvices = (predictionData.disease_data?.care_advices || []).map(item => ({
        advice: item.title,
        relevance_reason: item.why
      }));

      const enhancedData = {
        ...predictionData,
        disease_data: {
          ...predictionData.disease_data,
          care_advices: transformedCareAdvices
        }
      };

      setData(enhancedData);
      setLoading(false);
    } else {
      navigate("/diagnosis", { replace: true });
    }

    return () => {
      sessionStorage.removeItem("predictionResult");
    };
  }, [location.state, navigate]);

  const getConfidenceColor = (confidence) => {
    const percentage = confidence * 100;
    if (percentage >= 90) return "bg-green-500";
    if (percentage >= 70) return "bg-yellow-500";
    return "bg-red-500";
  };

  const getSeverityColor = (severity) => {
    switch (severity?.toLowerCase()) {
      case 'severe':
        return 'bg-red-100 text-red-800 border-red-300';
      case 'moderate':
        return 'bg-yellow-100 text-yellow-800 border-yellow-300';
      case 'mild':
        return 'bg-green-100 text-green-800 border-green-300';
      case 'none':
        return 'bg-blue-100 text-blue-800 border-blue-300';
      default:
        return 'bg-gray-100 text-gray-800 border-gray-300';
    }
  };

  const formatArrayItems = (items) => {
    if (!items) return [];
    if (Array.isArray(items)) return items;
    if (typeof items === 'string') {
      return items.split('\n').map(line => line.replace('• ', '').trim()).filter(Boolean);
    }
    return [];
  };

  if (loading) {
    return <DiagnosisLoader />;
  }

  if (!data) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <AlertTriangle className="w-16 h-16 text-red-500 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-800 mb-2">
            No Prediction Data Found
          </h2>
          <p className="text-gray-600 mb-4">
            Please upload an image first to get a diagnosis.
          </p>
          <button
            onClick={() => navigate("/diagnosis")}
            className="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition-colors"
          >
            Go to Diagnosis Page
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 p-4 sm:p-6">
      <div className="max-w-7xl mx-auto space-y-8">
        {/* Hero Section */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-3xl shadow-2xl overflow-hidden"
        >
          <div className="grid grid-cols-1 lg:grid-cols-2">
            {/* Image Section */}
            <div className="relative h-80 lg:h-full">
              <img
                src={data.image_url}
                alt="Plant diagnosis"
                className="w-full h-full object-cover"
              />
              <div className="absolute top-4 right-4">
                <div className={`px-4 py-2 rounded-full font-semibold text-white shadow-lg ${getConfidenceColor(data.confidence)}`}>
                  {(data.confidence * 100).toFixed(1)}% Confidence
                </div>
              </div>
            </div>

            {/* Info Section */}
            <div className="p-8 lg:p-12 flex flex-col justify-center space-y-6">
              <div>
                <p className="text-sm text-gray-500 uppercase tracking-wide mb-2">
                  Plant Type
                </p>
                <h2 className="text-3xl font-bold text-gray-800">
                  {data.disease_data.plant_name}
                </h2>
              </div>

              <div>
                <p className="text-sm text-gray-500 uppercase tracking-wide mb-2">
                  Diagnosis
                </p>
                <h1 className="text-4xl font-bold text-red-600 mb-2">
                  {data.disease_data.disease_name}
                </h1>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Disease Details Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Description */}
          {data.disease_data?.description && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 }}
              className="bg-white rounded-3xl shadow-lg p-6"
            >
              <h2 className="text-xl font-semibold mb-4 text-green-600 flex items-center">
                <AlertTriangle className="mr-2 w-6 h-6" />
                Description
              </h2>
              <p className="text-gray-700 leading-relaxed">
                {data.disease_data.description}
              </p>
            </motion.div>
          )}

          {/* Symptoms */}
          {data.disease_data?.symptoms && data.disease_data.symptoms.length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.15 }}
              className="bg-white rounded-3xl shadow-lg p-6"
            >
              <h2 className="text-xl font-semibold mb-4 text-green-600 flex items-center">
                <Bug className="mr-2 w-6 h-6" />
                Symptoms
              </h2>
              <ul className="space-y-2 list-disc list-inside">
                {formatArrayItems(data.disease_data.symptoms).map((symptom, idx) => (
                  <li key={idx} className="text-gray-700">{symptom}</li>
                ))}
              </ul>
            </motion.div>
          )}

          {/* Causes */}
          {data.disease_data?.causes && data.disease_data.causes.length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
              className="bg-white rounded-3xl shadow-lg p-6"
            >
              <h2 className="text-xl font-semibold mb-4 text-purple-600 flex items-center">
                <Lightbulb className="mr-2 w-6 h-6" />
                Causes
              </h2>
              <ul className="space-y-2 list-disc list-inside">
                {formatArrayItems(data.disease_data.causes).map((cause, idx) => (
                  <li key={idx} className="text-gray-700">{cause}</li>
                ))}
              </ul>
            </motion.div>
          )}

          {/* Spread Mechanisms */}
          {data.disease_data?.spread_mechanisms && data.disease_data.spread_mechanisms.length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.25 }}
              className="bg-white rounded-3xl shadow-lg p-6"
            >
              <h2 className="text-xl font-semibold mb-4 text-blue-600 flex items-center">
                <Wind className="mr-2 w-6 h-6" />
                How It Spreads
              </h2>
              <ul className="space-y-2 list-disc list-inside">
                {formatArrayItems(data.disease_data.spread_mechanisms).map((spread, idx) => (
                  <li key={idx} className="text-gray-700">{spread}</li>
                ))}
              </ul>
            </motion.div>
          )}
        </div>

        {/* Care Recommendations */}
        {data.disease_data?.care_advices && data.disease_data.care_advices.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="bg-white rounded-3xl shadow-lg p-8"
          >
            <h2 className="text-2xl font-bold mb-6 text-green-700 flex items-center">
              <Leaf className="mr-3 w-7 h-7" />
              Care Recommendations
            </h2>
            <div className="space-y-4">
              {data.disease_data.care_advices.map((item, index) => (
                <CareAdviceItem key={index} item={item} index={index} />
              ))}
            </div>
          </motion.div>
        )}

        {/* Action Button */}
        <div className="flex justify-center pb-8">
          <button
            className="bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 text-white py-4 px-8 rounded-xl font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300"
            onClick={() => navigate("/diagnosis")}
          >
            Diagnose Another Plant
          </button>
        </div>
      </div>
    </div>
  );
};

export default Prediction;
