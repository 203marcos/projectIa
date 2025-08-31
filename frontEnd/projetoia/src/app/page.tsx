"use client";

import { useState, useEffect } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ScatterChart,
  Scatter,
} from "recharts";
import { Calculator, TrendingUp, FileText, BarChart3, Beaker } from "lucide-react";


// Tipos para os dados vindos da API
type ModelResults = {
  coefficients: number[];
  r2: number;
  r2_adjusted: number;
  rmse: number;
  mse: number;
  mae: number;
};
type AlternativeModel = {
  r2: number;
  rmse: number;
  mse: number;
  mae: number;
};
type Residual = {
  obs: number;
  observed: number;
  predicted: number;
  residual: number;
};





export default function ArsenicAnalysisDashboard() {

  // Estados para dados vindos da API
  const [modelResults, setModelResults] = useState<ModelResults>({
    coefficients: [0, 0, 0, 0, 0],
    r2: 0,
    r2_adjusted: 0,
    rmse: 0,
    mse: 0,
    mae: 0,
  });
  const [alternativeModel, setAlternativeModel] = useState<AlternativeModel>({
    r2: 0,
    rmse: 0,
    mse: 0,
    mae: 0,
  });
  const [residualsData, setResidualsData] = useState<Residual[]>([]);


  const [predictionInputs, setPredictionInputs] = useState({
    idade: "30",
    usoBeber: "5",
    usoCozinhar: "5",
    arsenioAgua: "0.135",
  });

  // Atualiza scatterData dinamicamente
  const scatterData = residualsData.map((item) => ({
    predicted: item.predicted,
    observed: item.observed,
  }));
  const [prediction, setPrediction] = useState<number | null>(null);

  // Buscar dados da API ao montar
  useEffect(() => {
    fetch("http://localhost:8000/api/modelo")
      .then((res) => res.json())
      .then((data) => setModelResults(data));

    fetch("http://localhost:8000/api/modelo-alternativo")
      .then((res) => res.json())
      .then((data) => setAlternativeModel(data));

    fetch("http://localhost:8000/api/residuos")
      .then((res) => res.json())
      .then((data) => setResidualsData(data));
  }, []);

  // Predição via API
  const handlePredict = () => {
    fetch("http://localhost:8000/api/predizer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        idade: Number(predictionInputs.idade),
        usoBeber: Number(predictionInputs.usoBeber),
        usoCozinhar: Number(predictionInputs.usoCozinhar),
        arsenioAgua: Number(predictionInputs.arsenioAgua),
      }),
    })
      .then((res) => res.json())
      .then((data) => setPrediction(data.prediction));
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b bg-card">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center gap-3">
            <div className="flex items-center justify-center w-10 h-10 bg-primary rounded-lg">
              <Beaker className="w-6 h-6 text-primary-foreground" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-foreground">Análise de Arsênio</h1>
              <p className="text-sm text-muted-foreground">Dashboard de Regressão Linear Múltipla</p>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-6 py-8">
        {/* Métricas Principais */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">R² Score</CardTitle>
              <TrendingUp className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-primary">{modelResults.r2.toFixed(4)}</div>
              <p className="text-xs text-muted-foreground">Coeficiente de determinação</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">R² Ajustado</CardTitle>
              <BarChart3 className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-primary">{modelResults.r2_adjusted.toFixed(4)}</div>
              <p className="text-xs text-muted-foreground">Penaliza variáveis irrelevantes</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">RMSE</CardTitle>
              <Calculator className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{modelResults.rmse.toFixed(4)}</div>
              <p className="text-xs text-muted-foreground">Raiz do erro quadrático médio</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">MAE</CardTitle>
              <FileText className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{modelResults.mae.toFixed(4)}</div>
              <p className="text-xs text-muted-foreground">Erro absoluto médio</p>
            </CardContent>
          </Card>
        </div>

        <Tabs defaultValue="model" className="space-y-6">
          <TabsList className="grid w-full grid-cols-4">
            <TabsTrigger value="model">Modelo</TabsTrigger>
            <TabsTrigger value="prediction">Predição</TabsTrigger>
            <TabsTrigger value="residuals">Resíduos</TabsTrigger>
            <TabsTrigger value="comparison">Comparação</TabsTrigger>
          </TabsList>

          <TabsContent value="model" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle>Coeficientes do Modelo</CardTitle>
                  <CardDescription>
                    Modelo: Arsênio_Unhas = β₀ + β₁×Idade + β₂×Uso_Beber + β₃×Uso_Cozinhar + β₄×Arsênio_Água
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center">
                      <span className="text-sm font-medium">Intercepto (β₀)</span>
                      <Badge variant="outline">{modelResults.coefficients[0].toFixed(4)}</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-sm font-medium">Idade (β₁)</span>
                      <Badge variant="outline">{modelResults.coefficients[1].toFixed(4)}</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-sm font-medium">Uso Beber (β₂)</span>
                      <Badge variant="outline">{modelResults.coefficients[2].toFixed(4)}</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-sm font-medium">Uso Cozinhar (β₃)</span>
                      <Badge variant="outline">{modelResults.coefficients[3].toFixed(4)}</Badge>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-sm font-medium">Arsênio Água (β₄)</span>
                      <Badge variant="outline">{modelResults.coefficients[4].toFixed(4)}</Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>Gráfico de Dispersão</CardTitle>
                  <CardDescription>Valores Observados vs Preditos</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <ScatterChart data={scatterData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="predicted" name="Predito" />
                      <YAxis dataKey="observed" name="Observado" />
                      <Tooltip cursor={{ strokeDasharray: "3 3" }} />
                      <Scatter dataKey="observed" fill="hsl(var(--primary))" />
                    </ScatterChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="prediction" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Fazer Predição</CardTitle>
                <CardDescription>
                  Insira os valores das variáveis para prever a concentração de arsênio nas unhas
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="idade">Idade (anos)</Label>
                    <Input
                      id="idade"
                      type="number"
                      value={predictionInputs.idade}
                      onChange={(e) => setPredictionInputs((prev) => ({ ...prev, idade: e.target.value }))}
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="usoBeber">Uso para Beber (1-5)</Label>
                    <Input
                      id="usoBeber"
                      type="number"
                      min="1"
                      max="5"
                      value={predictionInputs.usoBeber}
                      onChange={(e) => setPredictionInputs((prev) => ({ ...prev, usoBeber: e.target.value }))}
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="usoCozinhar">Uso para Cozinhar (1-5)</Label>
                    <Input
                      id="usoCozinhar"
                      type="number"
                      min="1"
                      max="5"
                      value={predictionInputs.usoCozinhar}
                      onChange={(e) => setPredictionInputs((prev) => ({ ...prev, usoCozinhar: e.target.value }))}
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="arsenioAgua">Arsênio na Água (ppm)</Label>
                    <Input
                      id="arsenioAgua"
                      type="number"
                      step="0.001"
                      value={predictionInputs.arsenioAgua}
                      onChange={(e) => setPredictionInputs((prev) => ({ ...prev, arsenioAgua: e.target.value }))}
                    />
                  </div>
                </div>
                <Button onClick={handlePredict} className="w-full">
                  Calcular Predição
                </Button>
                {prediction !== null && (
                  <Card className="bg-primary/5 border-primary/20">
                    <CardContent className="pt-6">
                      <div className="text-center">
                        <p className="text-sm text-muted-foreground mb-2">Concentração Predita de Arsênio nas Unhas</p>
                        <p className="text-3xl font-bold text-primary">{prediction.toFixed(4)} ppm</p>
                      </div>
                    </CardContent>
                  </Card>
                )}
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="residuals" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle>Tabela de Resíduos</CardTitle>
                  <CardDescription>Análise dos resíduos para verificação das suposições do modelo</CardDescription>
                </CardHeader>
                <CardContent>
                  <Table>
                    <TableHeader>
                      <TableRow>
                        <TableHead>Obs.</TableHead>
                        <TableHead>Observado</TableHead>
                        <TableHead>Predito</TableHead>
                        <TableHead>Resíduo</TableHead>
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {residualsData.map((row) => (
                        <TableRow key={row.obs}>
                          <TableCell>{row.obs}</TableCell>
                          <TableCell>{row.observed.toFixed(4)}</TableCell>
                          <TableCell>{row.predicted.toFixed(4)}</TableCell>
                          <TableCell className={row.residual > 0 ? "text-green-600" : "text-red-600"}>
                            {row.residual.toFixed(4)}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>Gráfico de Resíduos</CardTitle>
                  <CardDescription>Distribuição dos resíduos</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={residualsData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="obs" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="residual" fill="hsl(var(--chart-1))" />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="comparison" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Comparação de Modelos</CardTitle>
                <CardDescription>Modelo Completo vs Modelo Alternativo (apenas Arsênio na Água)</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-4">
                    <h3 className="text-lg font-semibold text-primary">Modelo Completo</h3>
                    <div className="space-y-2">
                      <div className="flex justify-between">
                        <span>R²:</span>
                        <Badge variant="default">{modelResults.r2.toFixed(4)}</Badge>
                      </div>
                      <div className="flex justify-between">
                        <span>RMSE:</span>
                        <Badge variant="default">{modelResults.rmse.toFixed(4)}</Badge>
                      </div>
                      <div className="flex justify-between">
                        <span>MAE:</span>
                        <Badge variant="default">{modelResults.mae.toFixed(4)}</Badge>
                      </div>
                    </div>
                  </div>
                  <div className="space-y-4">
                    <h3 className="text-lg font-semibold text-primary">Modelo Alternativo</h3>
                    <div className="space-y-2">
                      <div className="flex justify-between">
                        <span>R²:</span>
                        <Badge variant="default">{alternativeModel.r2.toFixed(4)}</Badge>
                      </div>
                      <div className="flex justify-between">
                        <span>RMSE:</span>
                        <Badge variant="default">{alternativeModel.rmse.toFixed(4)}</Badge>
                      </div>
                      <div className="flex justify-between">
                        <span>MAE:</span>
                        <Badge variant="default">{alternativeModel.mae.toFixed(4)}</Badge>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="mt-6 p-4 bg-muted rounded-lg">
                  <p className="text-sm text-muted-foreground">
                    <strong>Conclusão:</strong> O modelo completo apresenta melhor performance com R² ={" "}
                    {modelResults.r2.toFixed(4)}
                    comparado ao modelo alternativo com R² = {alternativeModel.r2.toFixed(4)}. O RMSE também é menor no
                    modelo completo, indicando melhor precisão nas predições.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
