import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import React from "react"
import axios from 'axios';
export default function Home() {
  const [imageFile, SetImageFile] = React.useState("");
  const [data, SetData] = React.useState([])
  const InputEle = React.useRef();
  const HandlePredictImage = async function (fileImage: File) {
    try {
      let formData = new FormData();
      formData.append("image", fileImage);
      let result = await axios.post(`http://127.0.0.1:5000/upload`, formData,
        {
          headers: { "Content-Type": "multipart/form-data", 'Access-Control-Allow-Origin': '*' },
        })
      SetData(result.data)
      console.log(result.data[0])
    } catch (error) {

    }
  }
  return (
    <>
      <div className='w-screen h-screen '>
        <div className='h-[200px] flex justify-center flex-col items-center mb-10'>
          <div className='w-[200px] h-[200px] overflow-hidden'>
            <img src={imageFile}
              className=' w-full h-auto object-contain' alt="" />
          </div>
          <input onChange={async (e) => {
            let files = e.target.files as any
            console.log()
            SetImageFile(URL.createObjectURL(files[0] as Blob))
            await HandlePredictImage(e.target.files?.item(0) as File)
          }} type="file" id="" />
        </div>

        <div className='px-3 py-2 flex flex-wrap'>
          {
            data.map((item, index) => {
              return <>
                <div className='basis-1/5 md:basis-1/4 basis-1/2 h-[300px] p-2'>
                  <div className='h-full w-full'>
                    <img className='h-full w-full object-contain' src={`http://127.0.0.1:5000/images/${item[0].replace("./datasets/images_original\\","")}`} alt="" />
                  </div>
                </div>
              </>
            })
          }

        </div>



      </div>


    </>
  )
}
