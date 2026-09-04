from app.main import main
import asyncio
# função de execução do código 
if __name__ == "__main__":
	try:
		asyncio.run(main())
	
	except asyncio.TimeoutError as e:
		print(f'Limite de tempo atingido para execução: {e}')
	except asyncio.CancelledError as e:
		print(f'Task cancelada antes da execução: {e}')
	except asyncio.InvalidStateError as e:
		print(f'Operação inválida no estado de execução: {e}')
	except Exception as e:
		print(f"An error on run occurred: {e}")