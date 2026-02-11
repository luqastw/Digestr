import express from 'express'
import healthRoute from './routes/health'

const app = express()
const port = 3000

app.use('/health', healthRoute)
app.listen(port, () => {
    console.log(`Rodando na porta ${port}`)
})