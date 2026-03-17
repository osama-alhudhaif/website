import axiosInstance from "./__base__/axiosInstance";

export interface QalamMessage {
  id: number;
  role: "system" | "user" | "assistant";
  content: string;
  created_at: string;
}

export interface QalamSession {
  id: number;
  mode: string;
  story: number | null;
  created_at: string;
  updated_at: string;
  messages: QalamMessage[];
}

export interface QalamChatPayload {
  session_id?: number;
  message: string;
  mode?: string;
  story_id?: number;
}

export async function sendQalamMessage(payload: QalamChatPayload) {
  const response = await axiosInstance.post<QalamSession>("qalam/chat/", payload);
  return response.data;
}

