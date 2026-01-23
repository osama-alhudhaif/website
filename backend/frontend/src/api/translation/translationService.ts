// frontend/src/api/translation/translationService.ts
import axiosInstance from '../__base__/axiosInstance';
// import { ExampleType } from '../../types/Example'; // ??????? ???????

// ???? ????? ??? ????????
export const getExampleData = async () => {
  const response = await axiosInstance.get('/translation/example/');
  return response.data;
};
